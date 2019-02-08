import re
from django.test import TestCase
from ..Email import Email

# Create your tests here.
class TestGetEmail(TestCase):

     """
   def testMain(self):
        enterUrl = "football"
        Email.__init__(Email)
        finalData1 = "YOU ENTERED A GOOD URL!!"
        result = Email.main(Email, enterUrl)
        self.assertEquals(result, finalData1)"""

     def getEmail(self):

        Email.__init__(Email)

        urls = ["football.com", "itkamer.com"]
        enterUrl = "football"
        #finalData2 = " "

        result = Email.getEmail(Email, urls, enterUrl)
        self.assertEquals(result, finalData2)
