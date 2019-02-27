from django.test import TestCase
from ..FileManager import FileManager
import re


class TestFileManager(TestCase):

    def testsreadFile(self):
        url = "itkamer.com"
        #domainFile = r"E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\DomainsName\Domain.txt"
        fileContent = FileManager.readFile(FileManager,url)
        print(fileContent)


