import re
from django.test import TestCase
from ..FileManager import FileManager
# Create your tests here.
class TestFileManager(TestCase):

#method test getFiveFirstEmail

    def testgetFiveFirstEmail(self):
        testurl = 'itkamer.com'
        FileManager.__init__(FileManager)
        result = FileManager.getFiveFirstEmail(FileManager, testurl)
        self.assertEqual(len(result), 0)

    
