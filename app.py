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
    '/parse/(.*)', 'Parse',
    '/addentry/(.*)', 'AddEntry',
    '/bibtextosql/(.*)', 'BibTeXtoSQL',
    '/entrytobibtex/(.*)', 'EntryToBibTeX',
    '/previewentry/(.*)', 'PreviewEntry',
    '/setdoi/(.*)', 'SetDOI',
    '/validateentry/(.*)', 'ValidateEntry',
    '/import/(.*)', 'Import',
    '/', 'index'
)

#TODO: Add methods for ReLiS. Import, Format, Preview?, toSQL,

class index:
    def GET(self):
        return render.index()

class FormatBibTeX:
    def GET(self, code):
        return BiBlerApp.formatBibTeX(self, code)


class Parse:
    def GET(self, code):
        parser=BibTeXParser(code)
        return parser.parse().validate()

#BibTeX example: @book{,author={Adams},title={H2G2},year={1978}}
class AddEntry:
    def GET(self, code):
        return BiBlerWrapper.addEntry(self, code)

class EntryToBibTeX:
    def GET(self, code):
        return BiBlerWrapper.entryToBibTeX(self, code)

class BibTeXtoSQL:
    def GET(self, code):
        return BiBlerWrapper.bibtexToSQL(self, code)

class PreviewEntry:
    def GET(self, code):
        return BiBlerWrapper.previewEntry(self,code)

class SetDOI:
    def GET(self, code):
        return BiBlerWrapper.setDOI(self, code)

class ValidateEntry:
    def GET(self, code):
        return BiBlerWrapper.validateEntry(self, code)
class Import:
    def GET(self, code):
        return 'Unsupported'
        
'''class parse:
    def GET(self, code):
        return BibTeXParser.BibTeXParser(self, code).parse(self).validate(self)
'''        
web.webapi.internalerror = web.debugerror


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
if __name__ == '__main__': app.run()