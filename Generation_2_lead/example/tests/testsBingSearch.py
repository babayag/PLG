from django.test import TestCase
from ..FileManager import FileManager
from ..Email import Email
from ..BingSearch import BingSearch
import re

class TestBingSearch(TestCase):

    def testUrlValidDomain(self):
        print("test when the url is a vaildate domain")
        actualResult = BingSearch.UrlValidation(BingSearch,"itkamer.com")
        expectResult = True
        self.assertEqual(actualResult,expectResult)

    def testUrlValidWrong(self):
        print("test when the url is a wrong ")
        actualResult = BingSearch.UrlValidation(BingSearch,"aaaaaaaa")
        expectResult = False
        self.assertEqual(actualResult,expectResult)

    def testUrlValidationSSLDomain(self):
        print("test when the url is a ssl")
        actualResult = BingSearch.UrlValidation(BingSearch,"https://forbes.com")
        expectResult = True
        self.assertEqual(actualResult,expectResult)
    
<<<<<<< HEAD
    def testUrlValidationNoSSLDomain(self):
        print("test when the url is a  no ssl")
        actualResult = BingSearch.UrlValidation(BingSearch,"http://forbes.com")
        expectResult = True
        self.assertEqual(actualResult,expectResult)

    # def testextractGoodDomainSSL(self):
    #     print("extrat the domain when url is ssl format")
    #     actualResult = BingSearch.extractGoodDomain(BingSearch,"https//www.forbes.com")
    #     expectResult = "forbes.com"
    #     self.assertEqual(actualResult,expectResult)
    
    # def testextractGoodDomainNoSSL(self):
    #     print("extrat the domain when url is no ssl format")
    #     actualResult = BingSearch.extractGoodDomain(BingSearch,"http//www.tala.com")
    #     expectResult = "tala.com"
    #     self.assertEqual(actualResult,expectResult)

    def testextractGoodDomainWWW(self):
        print("extrat the domain when url has www.")
        actualResult = BingSearch.extractGoodDomain(BingSearch,"www.tala.com")
        expectResult = "tala.com"
        self.assertEqual(actualResult,expectResult)


    # def testWhenTherIsMorePages(self):
    #     numberOfPage = BingSearch.nbrPage(BingSearch,"football.com")

    #     self.assertEqual(len(numberOfPage),25)
    #     print('Good Test')
=======
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
        domainUrl2 = "httpsfg://www.google.com"
        domainUrl3 = "www.google.com"
        domainUrl4 = "google.eusebio.com"
        domainUrl5 = "http://google.com"
        domainUrl6 = "https://www.google.io"
        domainUrl7 = "https://us.google.io"

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
>>>>>>> ba19c19e6f356306e5ff576ddc65773213dbcf69

