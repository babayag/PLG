from django.test import TestCase
from ..FileManager import FileManager
import os
import json
from datetime import datetime
import time
from example.tests import *

# Create your tests here.


class Test(TestCase):
   
    def test_WriteInFile(self):

        FileManager.__init__(FileManager)
        data = [{'email': 'contact@paness-iiht.com', 'url': ['https://docs.google.com']}]
        enterUrl = "paness-iiht.com"
        LastpageNbr = 50
        canSearch = False
        finalData1 = True

        result = FileManager.WriteInFile(FileManager, data, enterUrl,LastpageNbr,canSearch)
        self.assertEquals(result, finalData1)

     def test_readFile(self):
        FileManager.__init__(FileManager)
        enterUrl = "itkamer.com"
        finalData = [{"email": "Isidore@itkamer.com", "url": ["https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869430589/name/Wanda%20POS%20Administrator%20Guide.pdf", "https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869433089/name/Wanda%20POS%20User%20Guide.pdf"]}, {"email": "isidore@itkamer.com", "url": ["https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869430589/name/Wanda%20POS%20Administrator%20Guide.pdf"]}, {"email": "sales@itkamer.com", "url": ["https://www.milesbeckler.com/products-products-product-secret-successful-marketing-answer/"]}, {"email": "tatiotir@itkamer.com", "url": ["https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869433089/name/Wanda%20POS%20User%20Guide.pdf", "https://sourceforge.net/projects/tatiotir/files/iDempiere/SetupScript/"]}, {"LastpageNbr": 50}, {"canSearch": True}]
        result = FileManager.readFile(FileManager,enterUrl)
        self.assertEquals(result, finalData)
    
    def test_GetLastPageNumber(self):
        FileManager.__init__(FileManager)
        enterUrl = "cr7.com"
        finalData2 = 21

        result = FileManager.GetLastPageNumber(FileManager,enterUrl)
        self.assertEquals(result, finalData2)

    def test_verifyIfFileExist(self):
        enterUrl = "football.com"
        finalData3 = True

        result = FileManager.verifyIfFileExist(FileManager, enterUrl)
        self.assertEquals(result, finalData3)
