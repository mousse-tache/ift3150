'''
@author: Felix Belanger Robillard
'''
#-*- coding: utf-8 -*-
import sys, os
import urllib.parse
abspath = os.path.dirname("/var/www/html/ift3150/")
sys.path.append(abspath)
os.chdir(abspath)
import web
from bibwrap import BiBlerWrapper

urls = (
    '/formatbibtex/(.*)', 'FormatBibTeX',
    '/addentry/(.*)', 'AddEntry',
    '/getbibtex/(.*)', 'GetBibTeX',
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
    def POST(self):

        return render.index()

class FormatBibTeX:
    def POST(self,code):
        data = web.data().decode()
        return BiBlerWrapper.formatBibtex(self,data)

class AddEntry:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.addEntry(self, data)

class GetBibTeX:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.getBibTeX(self, data)

class BibTeXtoSQL:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.bibtexToSQL(self, data)

class BibTeXtoCSV:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.bibtexToCSV(self, data)

class BibTeXtoHTML:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.bibtexToHTML(self, data)

class BibTeXtoBibTeX:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.bibtexTobibtex(self, data)

class PreviewEntry:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.previewEntry(self, data)

class ValidateEntry:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.validateEntry(self, data)
        
web.config.debug = True

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
if __name__ == '__main__': app.run()