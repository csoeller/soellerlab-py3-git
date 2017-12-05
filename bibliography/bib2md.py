#!/usr/bin/env python

### idea to use this approach came from http://valeriobasile.github.io/Managing-my-own-bibliography/
### which is gratefully acknowledged

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import convert_to_unicode

bibdb = 'CS-recent.bib'

def header():
    return """Title: Publications
Slug: publications

<img style="border-left:5px solid white" src="{filename}/images/research/cover-gallery.jpg" alt="Recent Journal Covers">

For an up-to-date bibliography with links to PDFs you can visit [Christian Soeller's Google Scholar page](http://scholar.google.co.uk/citations?hl=en&user=ByDRW44AAAAJ).

"""

def footer():
    return """

#### Older Publications

You can find older publications via [Christian Soeller's Google Scholar page](http://scholar.google.co.uk/citations?hl=en&user=ByDRW44AAAAJ).
"""

def normalise_authors(authstr):
    if ("," in authstr):
        authstrauthors = authstr.split(" and ")
        for ia, author in enumerate(authstrauthors):
            if ("," in author):
                authorparts = author.split(", ")
                # the first part [0] is last name, needs to become last
                # get and remove the first part, then append it as last
                lastname = authorparts.pop(0)
                authorparts.append(lastname)
                authorfirstlast = " ".join(authorparts)
                authstrauthors[ia] = authorfirstlast
        return ", ".join(authstrauthors)
    else:
        return authstr

def page_format(pagestr):
    newstr = pagestr.replace('--','-')
    return newstr

def icon(icostr):
    if icostr.startswith('fa'):
        icoclass = 'fa'
        icosize = 'fa-lg'
    elif icostr.startswith('ai'):
        icoclass = 'ai'
        icosize = 'ai-lg'
    else:
        raise RuntimeError('unkown icon type %s' % icostr)

    return '<i class="{0} {1} {2}"></i>'.format(icoclass,icostr,icosize)

# the bib file is generated automatically by Zotero
with open(bibdb) as bibtex_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    parser.homogenise_fields = False # ensure that 'url' fields are not renamed to 'link'
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

# print(bib_database.entries)

writer = BibTexWriter()
entries = {}
for bib_item in bib_database.entries:
    if 'booktitle' in bib_item:
        venue = u', __{}__'.format(bib_item['booktitle']).replace('{','').replace('}','')
    elif 'journal' in bib_item and bib_item['journal']:
        venue = u', __{}__'.format(bib_item['journal'])
    else:
        venue = u''
        
    if 'pages' in bib_item:
        if 'volume' in bib_item:
            pages = u', {}:{}'.format(bib_item['volume'],page_format(bib_item['pages']))
        else:
            pages = u', {}'.format(page_format(bib_item['pages']))
    else:
        pages = u''

    if 'file' in bib_item:
        pdf_link = u' [PDF]({})'.format(bib_item['file'].split(':')[1])
    else:
        pdf_link = u''

    if 'doi' in bib_item:
        doi_link = u'<a HREF=http://dx.doi.org/{0}>{1}</a>'.format(bib_item['doi'],icon('ai-doi'))
    else:
        doi_link = u''

    if 'url' in bib_item:
        if bib_item['url'].startswith('http'):
            url_link = u'<a HREF={0}>{1}</a>'.format(bib_item['url'],icon('fa-external-link-square'))
        else:
            url_link = u''
    else:
        url_link = u''

    # create bibtex file
    db = BibDatabase()
    db.entries = [bib_item]
    bib_file = 'bib/{0}.bib'.format(bib_item['ID'])
    bib_link = u' [bib]({})'.format(bib_file)
    bib_link = u''
    pdf_link = u''
    
    links = u''
    if url_link:
        links = links + u' ' + url_link
    if doi_link:
        links = links + u' ' + doi_link
    if pdf_link:
        links = links + u' ' + pdf_link
    if bib_link:
        links = links + u' ' + bib_link

    title = bib_item['title'].replace('{','').replace('}','')
    
    with open('{0}'.format(bib_file), 'w') as bib:
        bib.write(writer.write(db).encode('UTF-8'))


        if bib_item['year'] not in entries:
            entries[bib_item['year']] = []
        if not title.startswith('Shining new light on motoneurons'):
            entries[bib_item['year']].append(u"1. {0} *{1}* ({2}){3}{4}.{5}\n".
                                             format(normalise_authors(bib_item['author']),
                                                    title,
                                                    bib_item['year'],
                                                    venue,
                                                    pages,
                                                    links).encode('UTF-8'))




        
with open('publication_list.md', 'w') as md_file:
    md_file.write(header())
    for year in sorted(entries.keys(), reverse=True):
        md_file.write("\n\n#### %s\n\n" % year)
        md_file.write("\n".join(entries[year]))
    md_file.write(footer())
