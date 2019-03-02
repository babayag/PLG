from django.test import TestCase
from ..FileManager import FileManager
import re


class TestFileManager(TestCase):

    def test_WriteInFile(self):
        cacheFolderPath = r'E:\paness IIHT\M2\project\Nouveau dossier\PLG\Generation_2_lead\example\cache'
        #os.chdir(cacheFolderPath)   
        FileManager.__init__(FileManager)
        data = [{'email': 'contact@paness-iiht.com', 'url': ['https://docs.google.com']}]
        enterUrl = "itkamer.com"
        LastpageNbr = 50
        canSearch = True
        finalData1 = False

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
        enterUrl = "itkamer.com"
        finalData2 = 5

        result = FileManager.GetLastPageNumber(FileManager,enterUrl)
        self.assertEquals(result, finalData2)  
          
    def test_verifyIfFileExist(self):
        FileManager.__init__(FileManager)
        enterUrl = "football.com"
        finalData3 = True

        result = FileManager.verifyIfFileExist(FileManager, enterUrl)
        self.assertEquals(result, finalData3)    