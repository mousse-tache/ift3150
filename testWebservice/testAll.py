'''
Created on March 12, 2017
@author: Félix Bélanger-Robillard
'''
import unittest
from .testAddEntry import TestAddEntry
from .testExportSQL import TestExportSQL
from .testPreviewEntry import TestPreviewEntry
from .testExportCSV import TestExportCSV
from .testExportHTML import TestExportHTML
from .textExportBib import TestExportBib
from .testValidate import TestValidate
from .testFormatBibtex import TestFormatBibtex

def testApp():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddEntry))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPreviewEntry))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestExportSQL))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestExportCSV))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestExportHTML))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestExportBib))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestValidate))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFormatBibtex))
    return suite  


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testApp())