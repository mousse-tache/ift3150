'''
@author: Félix Bélanger-Robillard
'''
#-*- coding: utf-8 -*-
import sys, os
import urllib.parse
abspath = os.path.dirname("/var/www/ift3150/")
sys.path.append(abspath)
os.chdir(abspath)
import web
from bibwrap import BiBlerWrapper
render = web.template.render('templates', cache=False)

urls = (
    '/formatbibtex/(.*)', 'FormatBibTeX',
    '/addentry/(.*)', 'AddEntry',
    '/bibtextosql/(.*)', 'BibTeXtoSQL',
    '/bibtextocsv/(.*)', 'BibTeXtoCSV',
    '/bibtextohtml/(.*)', 'BibTeXtoHTML',
    '/bibtextobibtex/(.*)', 'BibTeXtoBibTeX',
    '/previewentry/(.*)', 'PreviewEntry',
    '/validateentry/(.*)', 'ValidateEntry',
    '/help/', 'index',
    '/', 'index'
)


'''
The following classes are used to handle the different URLs
'''
class index:
    def GET(self):
        return render.index()

class FormatBibTeX:
    def GET(self, code):
        return BiBlerWrapper.formatBibtex(self, urllib.parse.unquote_plus(code))

class AddEntry:
    def GET(self, code):
        return BiBlerWrapper.addEntry(self, urllib.parse.unquote_plus(code))

class BibTeXtoSQL:
    def GET(self, code):
        return BiBlerWrapper.bibtexToSQL(self, urllib.parse.unquote_plus(code))

class BibTeXtoCSV:
    def GET(self, code):
        return BiBlerWrapper.bibtexToCSV(self, urllib.parse.unquote_plus(code))

class BibTeXtoHTML:
    def GET(self, code):
        return BiBlerWrapper.bibtexToHTML(self, urllib.parse.unquote_plus(code))

class BibTeXtoBibTeX:
    def GET(self, code):
        return BiBlerWrapper.bibtexTobibtex(self, urllib.parse.unquote_plus(code))

class PreviewEntry:
    def GET(self, code):
        return BiBlerWrapper.previewEntry(self, urllib.parse.unquote_plus(code))

class ValidateEntry:
    def GET(self, code):
        return BiBlerWrapper.validateEntry(self, urllib.parse.unquote_plus(code))
        
web.config.debug = True

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
if __name__ == '__main__': app.run()