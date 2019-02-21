from django.test import TestCase
from ..FileManager import FileManager
from ..BingSearch import BingSearch
import re


class TestBingSearch(TestCase):

    '''def testUrlIsValid(self):
        url = BingSearch.UrlValidation(BingSearch,"itkamer.com")
        self.assertTrue(url)
        print("URL is correct!!")

    def testUrlIsNotValid(self):
        url = BingSearch.UrlValidation(BingSearch,"https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not")
        self.assertFalse(url)
        print("THE URL YOU ENTERED IS INCORRECT!!")

    def testWhenTherIsMorePages(self):
        numberOfPage = BingSearch.nbrPage(BingSearch,"football.com")

        self.assertEqual(len(numberOfPage),25)
        print('Good Test')
    def teststoreDomain(self):
        url = "itkamer.com"
        domainFile = "E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\DomainsName\Domain.txt"
        FileManager.storeDomain(FileManager,url)'''
    
    def testUrlValidation(self):
        domainUrl1 = "http://www.google.com"
        domainUrl2 = "https://www.google.com"
        domainUrl3 = "www.google.com"
        domainUrl4 = "itkamer.com"        

        expectedResult = True
        actualResult = BingSearch.UrlValidation(BingSearch, domainUrl1)
        self.assertEquals(actualResult, expectedResult)
        print("testUrlValidation")

    def testExtractGoodDomain(self):
        domainUrl1 = "http://www.google.com"
        domainUrl2 = "https://www.google.com"
        domainUrl3 = "www.google.com"
        domainUrl4 = "google.com"

        expectedResult = "google.com"
        actualResult = BingSearch.extractGoodDomain(BingSearch, domainUrl2)
        self.assertEquals(actualResult, expectedResult)
        print("testExtractGoodDomain")

    """def testNew(self):
        domainUrl1 = "com.itkamer"
        domainUrl2 = "itkamer"
        domainUrl3 = ""

        expectedResult = "google.com"
        actualResult = BingSearch.extractGoodDomain(BingSearch, domainUrl4)
        self.assertEquals(actualResult, expectedResult)"""

