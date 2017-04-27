'''
:Author: Felix Belanger Robillard

:module: The following classes are used to handle the different URLs


Pour utiliser l'ensemble de ces classes, on s'attend à ce que l'utilisateur 
cree passe par une requête http POST pour soumettre une reference BibTeX sous 
forme de string au webservice. Cette reference est ensuite ajoutee à une instance
locale de BiBler et sera ensuite traitee selon la methode appelee.

On ne peut appeler l'ensemble des methodes de l'API BiBler, les methodes pouvant être
appelees sont celles qui possèdent une classe equivalente au sein de ce module. Celles
qui ne sont pas disponibles sont celles qui necessitaient un identifiant pour
selectionner une entree en particulier, ce qui est caduque dans le format
actuel.
'''
#-*- coding: utf-8 -*-
import sys, os
import urllib.parse
abspath = os.path.dirname("/var/www/html/ift3150/")
sys.path.append(abspath)
os.chdir(abspath)
import web
from utils.settings import ExportFormat
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
    '/', 'index'
)
class index:
    def GET(self):
        return None

class FormatBibTeX:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
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
        return BiBlerWrapper.exportString(self, data, ExportFormat.SQL)

class BibTeXtoCSV:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.exportString(self, data, ExportFormat.CSV)

class BibTeXtoHTML:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode())
        return BiBlerWrapper.exportString(self, data, ExportFormat.HTML)

class BibTeXtoBibTeX:
    def POST(self,code):
        data = urllib.parse.unquote_plus(web.data().decode('utf-8'))
        return BiBlerWrapper.exportString(self, data, ExportFormat.BIBTEX)

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