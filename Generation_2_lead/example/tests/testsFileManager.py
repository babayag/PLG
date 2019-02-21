from django.test import TestCase
from ..FileManager import FileManager
import os
import json
from datetime import datetime
import time

# Create your tests here.


class Test(TestCase):
   
    def test_WriteInFile(self):

        FileManager.__init__(FileManager)
        data = [{'email': 'contact@paness-iiht.com', 'url': ['https://docs.google.com']}]
        enterUrl = "football.com"
        LastpageNbr = 50
        canSearch = False
        finalData1 = True

        result = FileManager.WriteInFile(FileManager, data, enterUrl,LastpageNbr,canSearch)
        self.assertEquals(result, finalData1)