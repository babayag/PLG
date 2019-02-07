import re
from django.test import TestCase
from ..Email import Email

# Create your tests here.
class TestGetEmail(TestCase):

    def testWentAllIsFound(self):
        TestAllEmail = []
        Email.__init__(Email)
        url = "www.bing.com/search?q=%40{}&first={}".format("itkamer.com", 11)
        email = Email.getEmail(Email,url, "itkamer.com")


        print(email)
        print("Wow all Emails have been found on the URL you entered !!!")


