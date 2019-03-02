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
        domainName = "itkamer.com"
        lastname = "roland"
        firstname = "nteguem"
        GenerateValidEmail.__init__(GenerateValidEmail)
        expecteddata = ['nroland@itkamer.com', 'nteguem.roland@itkamer.com', 'roland@itkamer.com', 
        'nteguem_roland@itkamer.com', 'n_roland@itkamer.com', 'nteguemr@itkamer.com', 'nteguem@itkamer.com', 
        'n@itkamer.com', 'r@itkamer.com', 'nr@itkamer.com', 'nteguemroland@itkamer.com', 'rolandnteguem@itkamer.com',
         'roland.nteguem@itkamer.com', 'rnteguem@itkamer.com']
        result = GenerateValidEmail.generatePossibleMailWithTwoEntry(
            GenerateValidEmail, firstname,lastname, domainName, listemailgenerate)
        self.assertEqual(result, expecteddata)
