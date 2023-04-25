import cssutils
sheet =  cssutils.parseFile('output/theme/css/style.css')
for rule in sheet.cssRules:
    try:
        if rule.selectorText == '#banner':
            rule.style.backgroundImage = 'url("https://physiologie.unibe.ch/~soeller/labsite/images/mybanner.png")'
            print(rule.cssText)
    except:
        pass

with open('output/theme/css/style.css', 'wb') as f:
    f.write(sheet.cssText)
