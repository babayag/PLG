import re
from django.test import TestCase
from ..Email import Email
from ..FileManager import FileManager
from ..BingSearch import BingSearch
# Create your tests here.
class TestGetEmail(TestCase):


    #test  method  returnTenEmails

    def testreturnTenEmails(self):

        pageurlsfirst = [[
             "/search?q=%40itkamer.com&first=1",
             "/search?q=%40itkamer.com&first=11",
             "/search?q=%40itkamer.com&first=21",
             "/search?q=%40itkamer.com&first=31",
             "/search?q=%40itkamer.com&first=41",
             "/search?q=%40itkamer.com&first=50"
         ], 1
         ]
        Email.__init__(Email)
        finalData = 10
        result = Email.returnTenEmails(Email, 0, pageurlsfirst)
        self.assertEquals(result, finalData)





