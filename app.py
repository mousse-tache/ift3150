#-*- coding: utf-8 -*-
import sys, os
abspath = os.path.dirname("/var/www/bibweb/")
sys.path.append(abspath)
os.chdir(abspath)
import web
from helpers import Helpers
render = web.template.render('templates', cache=False)

urls = (
    '/formatbibtex/(.*)', 'FormatBibTeX',
    '/parse/(.*)', 'Parse',
    '/addentry/(.*)', 'AddEntry',
    '/bibtextosql/(.*)', 'BibTeXtoSQL',
    '/entrytobibtex/(.*)', 'EntryToBibTeX',
    '/previewentry/(.*)', 'PreviewEntry',
    '/setdoi/(.*)', 'SetDOI',
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
        return Helpers.addEntry(self, code)

class EntryToBibTeX:
    def GET(self, code):
        return Helpers.entryToBibTeX(self, code)

class BibTeXtoSQL:
    def GET(self, code):
        return Helpers.bibtexToSQL(self, code)

class PreviewEntry:
    def GET(self, code):
        return Helpers.previewEntry(self,code)

class SetDOI:
    def GET(self, code):
        return Helpers.setDOI(self, code)
'''class parse:
    def GET(self, code):
        return BibTeXParser.BibTeXParser(self, code).parse(self).validate(self)
'''        
web.webapi.internalerror = web.debugerror


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
if __name__ == '__main__': app.run()