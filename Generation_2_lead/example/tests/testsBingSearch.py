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

