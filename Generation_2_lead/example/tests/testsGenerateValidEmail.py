import re
from django.test import TestCase
from ..GenerateValidEmail import GenerateValidEmail

# Create your tests here.


class TestsGenerateValidEmail(TestCase):

  # test testprintInvalidEntry method

    def testprintInvalidEntry(self):

        GenerateValidEmail.__init__(GenerateValidEmail)
        ValidEmail = GenerateValidEmail.printInvalidEntry(
            GenerateValidEmail, "domain.com", re.compile("^[\w\_\-\.\ ]+$"))
        self.assertEqual(ValidEmail, 0)

        # test testprintInvalidEntry method

    def testverifyEntry(self):

        GenerateValidEmail.__init__(GenerateValidEmail)
        verify = GenerateValidEmail.verifyEntry(
            GenerateValidEmail, "nteguem", "roland", "itkamer.com")
        self.assertEqual(verify, 0)
   
    def testgeneratePossibleMailWithTwoEntry(self):
      
        listemailgenerate = []
        GenerateValidEmail.__init__(GenerateValidEmail)
        GenerateValidEmail.generatePossibleMailWithTwoEntry(
            GenerateValidEmail, "nteguem", "roland", "itkamer.com", listemailgenerate)
        self.assertEqual(len(listemailgenerate), 14)
