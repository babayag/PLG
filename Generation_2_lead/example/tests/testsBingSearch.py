from django.test import TestCase
from ..FileManager import FileManager
import re


class TestBingSearch(TestCase):

   def testUrlIsValid(self):
        url = BingSearch.UrlValidation(BingSearch,"itkamer.com")
        self.assertTrue(url)
        print("URL is correct!!")


        
         