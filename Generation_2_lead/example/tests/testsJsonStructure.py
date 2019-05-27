from django.test import TestCase
from ..FileManager import FileManager
from ..JsonStructure import JsonStructure

class TestJsonStructure(TestCase):
    #------------------- Method getFiveFirstEmail() ------------------------------
    def testCanSearch(self):
        print("----------Tester la methode getFiveFirstEmail()---------")
        enterUrl = "football.com"
        data1 = [{"email": "Isidore@itkamer.com", "url": ["https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869433089/name/Wanda%20POS%20User%20Guide.pdf"]}, {"email": "sales@itkamer.com", "url": ["https://malingojunction.com/register-fr/", "https://www.milesbeckler.com/products-products-product-secret-successful-marketing-answer/"]}]
        data = [{"email": "fc-makuhari@football-com", "url": ["https://sosal.me/prefectures/12/cities/103/store_infos/200"]}, {"email": "fc-nagoya@football-com", "url": ["https://sosal.me/prefectures/23/cities/202/store_infos/482"]}, {"email": "filerhodgson@football.com", "url": ["https://d3recruitinghub.files.wordpress.com/2011/12/clint-dempsey-mock-resume1.pdf"]}, {"email": "fsf@football.com", "url": ["https://fotboltssamband-foroya.myshopify.com/pages/about-us"]}]
        FileManager.__init__(FileManager)
        fc = FileManager.readFile(FileManager, enterUrl)
        actualResult = JsonStructure.getFiveFirstEmail(JsonStructure, fc, data)
        expectedResult = 4
        self.assertEqual(actualResult, expectedResult)
        if expectedResult == 4:
            print("getFiveFirstEmail Working")

    
    #------------------- Method JsonStructureReturn() ------------------------------
    def testJsonStructureReturn(self):
        #JsonStructureReturn(self, Nemails, Nsources, enterUrl, LastpageNbr)
        print("----Test of the method JsonStructureReturn()-----")
        Nemails = ["first@email.com", "second@email.com", "third@email.com"]
        Nsources = ["https://firstsource.com", "https://secondsource.com", ["https://thirdSource1.com", "https://thirdSource2.com"]]
        enterUrl = "email.com"
        LastpageNbr = 10
        JsonStructure.__init__(JsonStructure)
        fileContent = JsonStructure.JsonStructureReturn(JsonStructure, Nemails, Nsources, enterUrl, LastpageNbr)
        print("file content")
        print(fileContent)

     #------------------- Method JsonStructureReturn() ------------------------------
    def testStructureMultipleDomains(self):
        #StructureMultipleDomains(self,Nemails, Nsources, goodUrl)
        print("----Test of the method StructureMultipleDomains()-----")
        Nemails = ["first@email.com", "second@email.com", "third@email.com"]
        Nsources = ["https://firstsource.com", "https://secondsource.com", "https://thirdSource1.com", "https://thirdSource2.com"]
        enterUrl = "email.com" 
        JsonStructure.__init__(JsonStructure)
        fileContent = JsonStructure.StructureMultipleDomains(JsonStructure, Nemails, Nsources, enterUrl)
        print("Structured")
        print(fileContent)  


        """ These two work but we will see better what is the entry for multiple sources  """
