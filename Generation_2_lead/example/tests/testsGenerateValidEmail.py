from django.test import TestCase
from ..GenerateValidEmail import GenerateValidEmail
import re

class TestGenerateValidEmail(TestCase):
    def test_generatePossibleMailWithOneEntry(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        name = "cindy"
        domainName = "cindy.com"
        listOfEmails = []
        finalData = ['c@cindy.com', 'cindy@cindy.com', '_cindy@cindy.com']

        result = GenerateValidEmail.generatePossibleMailWithOneEntry(GenerateValidEmail,name,domainName,listOfEmails)
        self.assertEquals(result, finalData) 

    def test_generatePossibleMail(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        firstname = "cindy"
        lastname = "sonfack"
        domainName = "cindy.com"
        finalData = ['c@cindy.com', 'cindy@cindy.com', '_cindy@cindy.com']

        result = GenerateValidEmail.generatePossibleMail(GenerateValidEmail,firstname,lastname,domainName)
        self.assertEquals(result, finalData) 

    def test_verifyEmail(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        email = "sonfackjoyce6@gmail.com"
        finalData = True

        result = GenerateValidEmail.verifyEmail(GenerateValidEmail,email)
        self.assertEquals(result, finalData) 

    def test_returnValidEmail(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        firstname = "cindy"
        lastname = "sonfack"
        domainName = "cindy.com"
        finalData = []

        result = GenerateValidEmail.returnValidEmail(GenerateValidEmail,firstname,lastname,domainName)
        self.assertEquals(result, finalData) 
