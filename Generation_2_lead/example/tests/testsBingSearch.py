from django.test import TestCase
from ..FileManager import FileManager
from ..Email import Email
from ..BingSearch import BingSearch
import re

 
class TestBingSearch(TestCase):

    """
    author : ????????
    params : MyUrl
    description : test the urlvalidation method (this method tell if url is good or not good and validate)
    but here we test only if the url is good
    return a boolean which confirm if url is good 
    """

    def testUrlValidDomain(self):
        print("test when the url is a vaildate domain")
        actualResult = BingSearch.UrlValidation(BingSearch,"itkamer.com")
        expectResult = True
        self.assertEqual(actualResult,expectResult)

    """
    author : ????????
    params : MyUrl
    description : test the urlvalidation method (this method tell if url is good or no good and validate)
    but here we test only if the url is not good
    return a boolean which confirm if url is not good
    """
    def testUrlValidWrong(self):
        print("test when the url is a wrong ")
        actualResult = BingSearch.UrlValidation(BingSearch,"aaaaaaaa")
        expectResult = False
        self.assertEqual(actualResult,expectResult)

    """
    author : ????????
    params : MyUrl
    description : test the urlvalidation method (this method tell if url is good or no good and validate)
    but here we test only if the url is a ssl
    return a boolean which confirm if url is a ssl
    """
    def testUrlValidationSSLDomain(self):
        print("test when the url is a ssl")
        actualResult = BingSearch.UrlValidation(BingSearch,"https://forbes.com")
        expectResult = True
        self.assertEqual(actualResult,expectResult)

    """  
    author : ????????
    params : MyUrl
    description : test the urlvalidation method (this method tell if url is good or no good and validate)
    but here we test only if the url is not a ssl
    return a boolean which confirm if url is not a ssl
    """
    
    def testUrlValidationNoSSLDomain(self):
        print("test when the url is a  no ssl")
        actualResult = BingSearch.UrlValidation(BingSearch,"http://forbes.com")
        expectResult = True
        self.assertEqual(actualResult,expectResult)

    # def testextractGoodDomainSSL(self):
    #     print("extrat the domain when url is ssl format")
    #     actualResult = BingSearch.ExtractGoodDomain(BingSearch,"https//www.forbes.com")
    #     expectResult = "forbes.com"
    #     self.assertEqual(actualResult,expectResult)
    
    # def testextractGoodDomainNoSSL(self):
    #     print("extrat the domain when url is no ssl format")
    #     actualResult = BingSearch.ExtractGoodDomain(BingSearch,"http//www.tala.com")
    #     expectResult = "tala.com"
    #     self.assertEqual(actualResult,expectResult)
    """
    author : ????????
    params : EnterUrl
    description :  test the method ExtractGoodDomain (this method extract a good domain when we enter an url)
    return the good domain
    """

    def testextractGoodDomainWWW(self):
        print("extrat the domain when url has www.")
        actualResult = BingSearch.ExtractGoodDomain(BingSearch,"www.tala.com")
        expectResult = "tala.com"
        self.assertEqual(actualResult,expectResult)


    # def testWhenTherIsMorePages(self):
    #     numberOfPage = BingSearch.nbrPage(BingSearch,"football.com")

    #     self.assertEqual(len(numberOfPage),25)
    #     print('Good Test')

