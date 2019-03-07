from django.test import TestCase
from ..FileManager import FileManager
from ..JsonStructure import JsonStructure

class TestJsonStructure(TestCase):
    def testCanSearch(self):
        print("Tester la methode Cansearch")
        enterUrl = "football.com"
        data1 = [{"email": "Isidore@itkamer.com", "url": ["https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869433089/name/Wanda%20POS%20User%20Guide.pdf"]}, {"email": "sales@itkamer.com", "url": ["https://malingojunction.com/register-fr/", "https://www.milesbeckler.com/products-products-product-secret-successful-marketing-answer/"]}]
        data = [{"email": "fc-makuhari@football-com", "url": ["https://sosal.me/prefectures/12/cities/103/store_infos/200"]}, {"email": "fc-nagoya@football-com", "url": ["https://sosal.me/prefectures/23/cities/202/store_infos/482"]}, {"email": "filerhodgson@football.com", "url": ["https://d3recruitinghub.files.wordpress.com/2011/12/clint-dempsey-mock-resume1.pdf"]}, {"email": "fsf@football.com", "url": ["https://fotboltssamband-foroya.myshopify.com/pages/about-us"]}]
        FileManager.__init__(FileManager)
        fc = FileManager.readFile(FileManager, enterUrl)
        actualResult = JsonStructure.getFiveFirstEmail(JsonStructure, fc, data)
        expectedResult = 0
        self.assertEqual(actualResult, expectedResult)
