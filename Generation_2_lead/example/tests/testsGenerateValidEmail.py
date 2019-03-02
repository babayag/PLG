from django.test import TestCase
from ..GenerateValidEmail import GenerateValidEmail
import re

class TestGenerateValidEmail(TestCase):

    def test_returnValidEmail(self):
        GenerateValidEmail.__init__(GenerateValidEmail)
        firstname = "cindy"
        lastname = "sonfack"
        domainName = "cindy.com"
        finalData = []

        result = GenerateValidEmail.returnValidEmail(GenerateValidEmail,firstname,lastname,domainName)
        self.assertEquals(result, finalData) 
