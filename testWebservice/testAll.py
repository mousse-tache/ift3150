'''
Created on March 12, 2017
@author: Félix Bélanger-Robillard
'''
import unittest
from testAddEntry import TestAddEntry
from testPreviewEntry import TestPreviewEntry
from testValidate import TestValidate
from testFormatBibtex import TestFormatBibtex

def testApp():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddEntry))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPreviewEntry))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestValidate))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFormatBibtex))
    return suite  


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testApp())