import unittest
import sys
sys.path.append('C:\\Users\\Amirgol\\courses\\python\\NBA_to_the_max')
from implementation.sanity_test import MyTest
from implementation.data_scrap_tests import DataScrapTests

def my_suite():
	suite = unittest.TestSuite()
	result = unittest.TestResult()
	suite.addTest(unittest.makeSuite(MyTest))
	suite.addTest(unittest.makeSuite(DataScrapTests))
	runner = unittest.TextTestRunner()
	print(runner.run(suite))


if __name__ == '__main__':
	my_suite()