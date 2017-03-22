'''
Created on March 10, 2017
@author: Félix Bélanger-Robillard
'''
import sys, os
abspath = os.path.dirname("/var/www/bibweb/")
sys.path.append(abspath)
os.chdir(abspath)

import unittest
from TestWebservice import oracle
from bibwrap import BiBlerWrapper


class TestAddEntry(unittest.TestCase):
    def setUp(self):
        #self.ui = BiBlerWrapper
        pass
    
    def tearDown(self):
        pass

    def testAddEmptyEntryFromNone(self):
        _id = BiBlerWrapper.addEntry(None)
        #self.assertIsNotNone(_id, 'empty entry not added.')
        #self.assertEqual(self.ui.getEntryCount(), 1, 'empty entry not added.')

    def testAddEmptyEntryFromEmptyString(self):
        _id = BiBlerWrapper.addEntry('')
        #self.assertIsNotNone(_id, 'empty entry not added.')
        #self.assertEqual(self.ui.getEntryCount(), 1, 'empty entry not added.')
        
    def testAddInEmptyEntryWithType(self):
        for t in EntryType.getAllEntryTypes():
            _id = self.ui.addEntry(None, t.lower())
            self.assertIsNotNone(_id, 'empty %s entry not added.' % t)

    def testAddValidBibTeX(self):
        for e in oracle.valid_bibtex_variants:
            _id = self.ui.addEntry(e.getBibTeX())
            self.assertIsNotNone(_id, '%s not added.' % e)

    def testAddInNonEmptyDB(self):
        for e in oracle.all_entry_types:
            self.ui.addEntry(e.getBibTeX())
        _id = self.ui.addEntry(oracle.valid_entry_full.getBibTeX())
        self.assertIsNotNone(_id, '%s not added.' % oracle.valid_entry_full)
        self.assertEqual(self.ui.getEntryCount(), len(oracle.all_entry_types) + 1, '%s not added.' % oracle.valid_entry_full)

    def testAddExistingEntry(self):
        entry = oracle.valid_entry_full
        self.ui.addEntry(entry.getBibTeX())
        _id = self.ui.addEntry(entry.getBibTeX())
        self.assertIsNotNone(_id, 'entry not added.')
        self.assertTrue(self.ui.getEntry(_id)[EntryListColumn.Entrykey].endswith('a'), 'incorrect key in duplicate of %s.' % entry)
        self.assertEqual(self.ui.getEntryCount(), 2, '%s not added.' % oracle.valid_entry_full)

    def testAddMissingRequiredField(self):
        for e in oracle.all_invalid_entry_types_no_req:
            _id = self.ui.addEntry(e.getBibTeX())
            self.assertIsNone(_id, '%s wrongly added.' % e)
            self.assertEqual(self.ui.getEntryCount(), 0, '%s wrongly added.' % e)

    def testAddInvalidBibTeX(self):
        for e in oracle.all_invalid_entry_types:
            _id = self.ui.addEntry(e.getBibTeX())
            self.assertIsNone(_id, '%s was wrongly added.' % e)
            self.assertEqual(self.ui.getEntryCount(), 0, '%s wrongly added.' % e)
    
    def testAddDeleteSanity(self):
        _id = self.ui.addEntry(oracle.valid_entry_full.getBibTeX())
        self.ui.deleteEntry(_id)
        self.assertEqual(self.ui.getEntryCount(), 0, 'adding an entry then deleting it did not undo the addition.')
    
    def testAddWithQuotes(self):
        settings.Preferences().overrideKeyGeneration = False
        _id = self.ui.addEntry(oracle.valid_entry_bracket.getBibTeX())
        bibtex_bracket = self.ui.getBibTeX(_id)
        _id = self.ui.addEntry(oracle.valid_entry_quote.getBibTeX())
        bibtex_quote = self.ui.getBibTeX(_id)
        self.assertEqual(bibtex_bracket, bibtex_quote, 'adding an entry in quotes does not parse correctly')


if __name__ == "__main__":
    unittest.main()