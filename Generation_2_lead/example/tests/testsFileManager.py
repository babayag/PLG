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

    
   def testsreadFile(self):
        url = "itkamer.com"
        #domainFile = r"E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\DomainsName\Domain.txt"
        fileContent = FileManager.readFile(FileManager,url)
        print(fileContent)
