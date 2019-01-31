from django.test import TestCase
from ..BingSearch import BingSearch
import re


class TestBingSearch(TestCase):

    def testUrlIsValid(self):
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


