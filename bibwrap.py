'''
@author: Felix Belanger Robillard
'''
#-*- coding: utf-8 -*-
#import sys, os
#abspath = os.path.dirname("/var/www/ift3150/app/")
#sys.path.append(abspath)
#os.chdir(abspath)
from app.user_interface import BiBlerApp
import tempfile


class BiBlerWrapper(object):
    @staticmethod
    def addEntry(self, bibtex):
        '''
        Takes a BibTeX string and outputs the corresponding EntryDict
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: L{EntryDict}.
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        biblerapp.addEntry(bibtex)
        return biblerapp.iterAllEntries()

    @staticmethod
    def getBibTeX(self, bibtex):
        '''
        Takes a BibTeX string and outputs the corresponding BibTex
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: L{EntryDict}.
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        b = biblerapp.addEntry(bibtex)
        return biblerapp.getBibTeX(b)


    @staticmethod
    def bibtexToSQL(self,bibtex):
        '''
        Takes a BibTeX string and outputs a SQL table
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: SQL file.
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        biblerapp.addEntry(bibtex)
        path="/var/www/html/ift3150/export/export.sql"
        biblerapp.exportFile(path, 'sql')
        try:
            f = open("/var/www/html/ift3150/export/export.sql", 'r')
            return f.read()
        except:
            return 'Error' # you can send an 404 error here if you want
    @staticmethod
    def bibtexToCSV(self,bibtex):
        '''
        Takes a BibTeX string and outputs a .csv file
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: CSV file.
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        biblerapp.addEntry(bibtex)
        path="/var/www/html/ift3150/export/export.csv"
        biblerapp.exportFile(path, 'csv')
        try:
            f = open("/var/www/html/ift3150/export/export.csv", 'r')
            return f.read()
        except:
            return 'Error' # you can send an 404 error here if you want
    @staticmethod
    def bibtexTobibtex(self,bibtex):
        '''
        Takes a BibTeX string and outputs a .bib file
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: BibTeX file.
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        biblerapp.addEntry(bibtex)
        path="/var/www/html/ift3150/export/export.bib"
        biblerapp.exportFile(path, 'bib')
        try:
            f = open(path, 'r')
            return f.read()
        except:
            return 'Error' # you can send an 404 error here if you want
    @staticmethod
    def bibtexToHTML(self,bibtex):
        '''
        Takes a BibTeX string and outputs a .html file
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: HTML file.
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        biblerapp.addEntry(bibtex)
        path="/var/www/html/ift3150/export/export.html"
        file=tempfile.NamedTemporaryFile(delete=False)
        biblerapp.exportFile(file, 'html')
        return file.read()

    @staticmethod
    def previewEntry(self,bibtex):
        '''
        Takes a BibTeX string and outputs an HTML preview
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: str.
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        entryid = biblerapp.addEntry(bibtex)
        return biblerapp.previewEntry(entryid)

    @staticmethod
    def validateEntry(self, bibtex):
        '''
        Takes a BibTeX string and outputs 1 if the entry is valid or 0 if it's not
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: boolean .
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp(self, bibtex)
        biblerapp.addEntry(bibtex)
        return biblerapp.validateAllEntries()
 

    @staticmethod
    def formatBibtex(self, bibtex):
        '''
        Takes a BibTeX string and outputs a formatted BibTeX
        @type bibtex: L{str}
        @param bibtex: The BibTeX string to be processed.
        @return: boolean .
        '''
        return BiBlerApp.formatBibTeX(self, bibtex)



    @staticmethod
    def __getBiblerApp(self, bibtex):
        '''
        Returns an instance of BiblerApp with proper settings and
        an entry based on the bibtex given
        '''
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        #bibtex=BiBlerApp.formatBibTeX(self, bibtex)
        return biblerapp
