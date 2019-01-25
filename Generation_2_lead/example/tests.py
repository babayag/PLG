import re

from django.test import TestCase

from .BingSearch import BingSearch

# Create your tests here.


class BingSearchTest(TestCase):
   def test_InvalidUrl(self):
       url = 'www.example.com'
       result = BingSearch.search(BingSearch, url)
       self.assertEqual(result, "No")

   def test_ValidUrl(self):
       url = 'http://www.example.com'
       result = BingSearch.search(BingSearch, url)
       self.assertEqual(result, "Yes")