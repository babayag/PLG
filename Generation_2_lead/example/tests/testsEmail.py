import re
from django.test import TestCase
from ..Email import Email



# Create your tests here.
class TestEmail(TestCase):


    def TestMain(self):
        enterUrl = "football"
        finalData = "YOU ENTERED A GOOD URL"

        result = Email.main(Email,enterUrl)
        self.assertEquals(result, finalData)
    """
    def getEmail(self):
        urls = ["football.com","itkamer.com"]
        enterUrl = "football.com"
        finalData

        result = Email.getEmail(Email,urls,enterUrl)
        self.assertEquals(result, finalData)
"""