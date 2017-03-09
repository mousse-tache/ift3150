#-*- coding: utf-8 -*-
#import sys, os
#abspath = os.path.dirname("/var/www/bibweb/app/")
#sys.path.append(abspath)
#os.chdir(abspath)
from app.user_interface import BiBlerApp
from app.bibtex_parser import BibTeXParser
from app.manager import ReferenceManager

class BiBlerWrapper(object):
    @staticmethod
    def addEntry(self, bibtex):
        '''
        Takes a @bibtex string and outputs the corresponding EntryDict
        '''
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        bibtex=BiBlerApp.formatBibTeX(self, bibtex)
        entryid=biblerapp.addEntry(bibtex)
        return biblerapp.getEntry(entryid)

    @staticmethod
    def bibtexToSQL(self,bibtex):
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        bibtex=BiBlerApp.formatBibTeX(self, bibtex)
        biblerapp.addEntry(bibtex)
        path="/var/www/bibweb/export/export.sql"
        biblerapp.exportFile(path, 'sql')
        try:
            f = open("/var/www/bibweb/export/export.sql", 'r')
            return f.read()
        except:
            return '' # you can send an 404 error here if you want
        

    @staticmethod
    def entryToBibTeX(self, entry):
        return Utilities.addEntry(self, entry).toBibTeX()

    @staticmethod
    def previewEntry(self,bibtex):
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        bibtex=BiBlerApp.formatBibTeX(self, bibtex)
        entryid = biblerapp.addEntry(bibtex)
        return biblerapp.previewEntry(entryid)

    @staticmethod
    def setDOI(self, entryBibTeX):
        entryBibTeX = Utilities.addEntry(self, entryBibTeX)
        manager=ReferenceManager()
        return manager.add(self, entryBibTeX)
        
    @staticmethod
    def validateEntry(self, bibtex):
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        bibtex=BiBlerApp.formatBibTeX(self, bibtex)
        biblerapp.addEntry(bibtex)
        return biblerapp.validateAllEntries() 
    @staticmethod
    def  importFile(self, code):
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        bibtex=BiBlerApp.formatBibTeX(self, bibtex)
        biblerapp.addEntry(bibtex)
        path="/var/www/bibweb/export/export"
        biblerapp.exportFile(path, 'sql')
        