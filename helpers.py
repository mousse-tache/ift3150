#-*- coding: utf-8 -*-
import sys, os
abspath = os.path.dirname("/var/www/bibweb/app/")
sys.path.append(abspath)
os.chdir(abspath)
from app.user_interface import BiBlerApp
from app.bibtex_parser import BibTeXParser
from app.impex import MySQLExporter
from app.manager import ReferenceManager

class Helpers(object):
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
        entryid=biblerapp.addEntry(bibtex)
        entries=biblerapp.getEntry(entryid)
        path="/"
        exporter=MySQLExporter(path, entries)
        return exporter_exportEntry(self, entryid)

    @staticmethod
    def entryToBibTeX(self, entry):
        return Helpers.addEntry(self, entry).toBibTeX()

    @staticmethod
    def previewEntry(self,bibtex):
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        bibtex=BiBlerApp.formatBibTeX(self, bibtex)
        entryid = biblerapp.addEntry(bibtex)
        return biblerapp.previewEntry(entryid)

    @staticmethod
    def setDOI(self, entryBibTeX):
        entryBibTeX = Helpers.addEntry(self, entryBibTeX)
        manager=ReferenceManager()
        return manager.add(self, entryBibTeX)

    	
