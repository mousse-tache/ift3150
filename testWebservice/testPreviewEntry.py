'''
Created on March 10, 2017
@author: Félix Bélanger-Robillard
'''
import sys, os
abspath = os.path.dirname("/var/www/bibweb/")
sys.path.append(abspath)
os.chdir(abspath)
from TestWebservice import oracle
from bibwrap import BiBlerWrapper


class TestPreviewEntry(unittest.TestCase):
    def setUp(self):
        self.ui = BiBlerApp()

    def tearDown(self):
        pass

    def testPreviewACMAllFields(self):
        Preferences().bibStyle = BibStyle.ACM
        for entry in oracle.all_entries_all_fields:
            _id = self.ui.addEntry(entry.getBibTeX())
            if _id:
                html = self.ui.previewEntry(_id)
                self.assertEqual(html, entry.getACM_HTML(), '%s was not previewed correctly.' % entry)

    def testPreviewACMMissingOptionalFields(self):
        Preferences().bibStyle = BibStyle.ACM
        for entry in oracle.all_entry_types:
            _id = self.ui.addEntry(entry.getBibTeX())
            if _id:
                html = self.ui.previewEntry(_id)
                self.assertEqual(html, entry.getACM_HTML(), '%s was not previewed correctly.' % entry)

    def testPreviewACMNonExistingEntry(self):
        Preferences().bibStyle = BibStyle.ACM
        _id = self.ui.addEntry(oracle.valid_entry_full.getBibTeX())
        self.assertRaises(Exception, self.ui.previewEntry, _id + 1)
    
    def testPreviewACMAuthorVariants(self):
        Preferences().bibStyle = BibStyle.ACM
        for entry in oracle.valid_authors:
            _id = self.ui.addEntry(entry.getBibTeX())
            if _id:
                html = self.ui.previewEntry(_id)
                self.assertEqual(html, entry.getACM_HTML(), '%s was not previewed correctly.' % entry)


if __name__ == "__main__":
    unittest.main()