import re
from django.test import TestCase
from ..FileManager import FileManager
# Create your tests here.
class TestFileManager(TestCase):

#method test getFiveFirstEmail

    def testGetLastPageNumber(self):
        testurl = 'itkamer.com'
        FileManager.__init__(FileManager)
        result = FileManager.GetLastPageNumber(FileManager, testurl)
        self.assertEqual(result, 100)

    
