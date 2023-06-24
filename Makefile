PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=phy-lmsrv2.ex.ac.uk
SSH_PORT=22
SSH_USER=csoelle
SSH_TARGET_DIR=/home/csoelle/html

SMB_TARGET_DIR=/volumes/groupsoellerlabsite$$

S3_BUCKET=my_s3_bucket

CLOUDFILES_USERNAME=my_rackspace_username
CLOUDFILES_API_KEY=my_rackspace_api_key
CLOUDFILES_CONTAINER=my_cloudfiles_container

DROPBOX_DIR=~/Dropbox/Public/

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make ftp_upload                     upload the web site via FTP        '
	@echo '   make s3_upload                      upload the web site via S3         '
	@echo '   make cf_upload                      upload the web site via Cloud Files'
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '   make biblio                         rebuild publications.md            '
	@echo '                                                                          '
	@echo '   make smb_mount                      mount soellerlab as smb share      '
	@echo '   make smb_unmount                    unmount soellerlab smb share       '
	@echo '   make smb_upload                     upload the webste via smb - cp     '
	@echo '   make smb_rsync                      upload the webste via smb - rsync  '
	@echo '   make smb_clean                      remove files from soellerlab smb   '
	@echo '                                                                          '
	@echo '   make fix_bannner                    put banner image info into site.css'
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)


devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)


publish: clean
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	if [ -d $(OUTPUTDIR)/drafts ]; then rm -r $(OUTPUTDIR)/drafts; fi
	# python fix-site_css.py

biblio:
	if ! [ -d "bibliography/bib" ]; then echo "creating directory bibliography/bib" && mkdir bibliography/bib; fi
	cd bibliography && python bib2md.py zotero-export-cs-biblio.bib && cp publication_list.md $(INPUTDIR)/pages/publications.md

fix_banner: publish

ssh_upload: publish
	ssh $(SSH_USER)@$(SSH_HOST) 'mkdir $$HOME/html'
	# potential alternative
	# tar cf --exclude="*.pyc" --exclude=".[a-z]*" - /src/path | ssh userid@server.com tar xf - -C /dest/path
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

smb_mount:
	if ! [ -d $(SMB_TARGET_DIR) ]; then osascript -e "try" -e 'mount volume "smb://soeller@pc150.physio.unibe.ch/groupsoellerlabsite$$"' -e "end try"; fi

smb_unmount:
	if [ -d $(SMB_TARGET_DIR) ]; then diskutil unmount $(SMB_TARGET_DIR); fi

smb_clean:
	if [ -d $(SMB_TARGET_DIR) ]; then rm -rf $(SMB_TARGET_DIR)/*; fi

smb_ls:
	if [ -d $(SMB_TARGET_DIR) ]; then ls $(SMB_TARGET_DIR); fi

smb_upload: publish imgcompress
	if [ -d $(SMB_TARGET_DIR) ]; then scp -vr $(OUTPUTDIR)/* $(SMB_TARGET_DIR); fi

# note trailing slashes on directory names are critical
smb_rsync: publish imgcompress
	if [ -d $(SMB_TARGET_DIR) ]; then rsync -va --delete --exclude=.DS_Store $(OUTPUTDIR)/ $(SMB_TARGET_DIR)/; fi

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

s3_upload: publish
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type --no-mime-magic --no-preserve

cf_upload: publish
	cd $(OUTPUTDIR) && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

github: publish
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github

pngcompress:
	echo 'compressing pngs...'
	find $(OUTPUTDIR) -iname '*.png' -print0 | xargs -0 optipng -preserve -quiet

jpgcompress:
	echo 'compressing jpgs...'
	find $(OUTPUTDIR) -iname '*.jpg' -print0 | xargs -0 jpegoptim --strip-all --all-progressive --preserve --quiet --totals

imgcompress: pngcompress jpgcompress
