from django.test import TestCase
from ..GenerateValidEmail import GenerateValidEmail
import re

class TestGenerateValidEmail(TestCase):
    """
    author : Sonfack Cindy
    params : name ,domainName,listOfEmails  
    description :test the GeneratePossibleMailWithOneEntry method (thos method generate possible random email when we have one entry)  
    return:listOfEmails
    """
    def test_generatePossibleMailWithOneEntry(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        name = "cindy"
        domainName = "cindy.com"
        listOfEmails = []
        finalData = ['c@cindy.com', 'cindy@cindy.com', '_cindy@cindy.com']

        result = GenerateValidEmail.GeneratePossibleMailWithOneEntry(GenerateValidEmail,name,domainName,listOfEmails)
        self.assertEquals(result, finalData) 
    """
    author : Sonfack Cindy
    params : firstname,lastname,domainName 
    description :test the GeneratePossibleMailWithOneEntry method (thos method generate possible random email)  
    return:listOfEmails
    """
    def test_generatePossibleMail(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        firstname = "cindy"
        lastname = "sonfack"
        domainName = "cindy.com"
        finalData = ['c@cindy.com', 'cindy@cindy.com', '_cindy@cindy.com']

        result = GenerateValidEmail.GeneratePossibleMail(GenerateValidEmail,firstname,lastname,domainName)
        self.assertEquals(result, finalData) 

    """
    author : Sonfack Cindy
    params : email
    description :test the VerifyEmail method (this method  verify if email exist)  
    return: a boolean wich tell if email is exist or no 
    """
    def test_verifyEmail(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        email = "sonfackjoyce6@gmail.com"
        finalData = True

        result = GenerateValidEmail.VerifyEmail(GenerateValidEmail,email)
        self.assertEquals(result, finalData) 

    """
    author : Sonfack Cindy
    params : firstname,lastname,domainName
    description :test the ReturnValidEmail method (this method  Return valid email)  
    return:ValidEmails
    """
    def test_returnValidEmail(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        firstname = "cindy"
        lastname = "sonfack"
        domainName = "cindy.com"
        finalData = []

        result = GenerateValidEmail.ReturnValidEmail(GenerateValidEmail,firstname,lastname,domainName)
        self.assertEquals(result, finalData) 
