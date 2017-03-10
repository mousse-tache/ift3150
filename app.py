#-*- coding: utf-8 -*-
import sys, os
abspath = os.path.dirname("/var/www/bibweb/")
sys.path.append(abspath)
os.chdir(abspath)
import web
from bibwrap import BiBlerWrapper
render = web.template.render('templates', cache=False)

urls = (
    '/formatbibtex/(.*)', 'FormatBibTeX',
    '/addentry/(.*)', 'AddEntry',
    '/bibtextosql/(.*)', 'BibTeXtoSQL',
    '/previewentry/(.*)', 'PreviewEntry',
    '/validateentry/(.*)', 'ValidateEntry',
    '/help/', 'index'
)


'''
The following classes are used to handle the different URLs
'''
class index:
    def GET(self):
        return render.index()

class FormatBibTeX:
    def GET(self, code):
        return BiBlerWrapper.formatBibtex(self, code)

class Parse:
    def GET(self, code):
        BibwlerWrapper.parse(code) 

class AddEntry:
    def GET(self, code):
        return BiBlerWrapper.addEntry(self, code)

class BibTeXtoSQL:
    def GET(self, code):
        return BiBlerWrapper.bibtexToSQL(self, code)

class PreviewEntry:
    def GET(self, code):
        return BiBlerWrapper.previewEntry(self,code)

class ValidateEntry:
    def GET(self, code):
        return BiBlerWrapper.validateEntry(self, code)
        
web.config.debug = True

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
if __name__ == '__main__': app.run()