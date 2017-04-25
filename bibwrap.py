'''
:Author: Felix Belanger Robillard
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
        
        :param str bibtex: The BibTeX string to be processed.
        :return: The written Entry from the BibTeX
        :rtype: EntryDict
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp()
        biblerapp.addEntry(bibtex)
        return biblerapp.iterAllEntries()

    @staticmethod
    def getBibTeX(self, bibtex):
        '''

        Takes a BibTeX string and outputs the corresponding corrected BibTeX string
        
        :param str bibtex: The BibTeX string to be processed.
        :return: The corrected BibTeX including overriden key
        :rtype: str
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp()
        b = biblerapp.addEntry(bibtex)
        return biblerapp.getBibTeX(b)


    @staticmethod
    def exportString(self, bibtex, format):
        '''

        Takes a BibTeX string and outputs a string to the specified format
        
        :param str bibtex: The BibTeX string to be processed.
        :return: String to specified format
        :rtype: string
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp()
        biblerapp.addEntry(bibtex)
        return biblerapp.exportString(format)
         
    @staticmethod
    def previewEntry(self,bibtex):
        '''

        Takes a BibTeX string and outputs an HTML preview
        
        :param str bibtex: The BibTeX string to be processed.
        :return: HTML preview for the entry
        :rtype: str
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp()
        entryid = biblerapp.addEntry(bibtex)
        return biblerapp.previewEntry(entryid)

    @staticmethod
    def validateEntry(self, bibtex):
        '''

        Takes a BibTeX string and outputs 1 if the entry is valid or 0 if it's not

        :param str bibtex: The BibTeX string to be processed.
        :return: Number of valid entries, which will be 0 or 1
        :rtype: int
        '''
        biblerapp=BiBlerWrapper.__getBiblerApp()
        biblerapp.addEntry(bibtex)
        return biblerapp.validateAllEntries()
 

    @staticmethod
    def formatBibtex(self, bibtex):
        '''

        Takes a BibTeX string and outputs a formatted BibTeX

        :param str bibtex: The BibTeX string to be processed.
        :return: BibTeX entry
        :rtype: str
        '''
        return BiBlerApp.formatBibTeX(self, bibtex)



    @staticmethod
    def __getBiblerApp():
        '''

        Returns an instance of BiblerApp.

        :return: Bibler's API instance
        :rtype: BiblerApp
        '''
        biblerapp=BiBlerApp()
        biblerapp.preferences.overrideKeyGeneration = True
        return biblerapp
