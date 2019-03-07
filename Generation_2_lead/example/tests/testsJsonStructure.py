from  django.test import TestCase
from ..JsonStructure import JsonStructure
from ..FileManager import FileManager


class TestJsonStructure():

    def testgetFiveFirstEmail(self):

        enterUrl = "itkamer.com"
        FileManager.__init__(FileManager)
        filecontent = FileManager.readFile(FileManager,enterUrl)

        data = [{"email": "Isidore@itkamer.com", "url": ["https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869433089/name/Wanda%20POS%20User%20Guide.pdf"]}, {"email": "sales@itkamer.com", "url": ["https://malingojunction.com/register-fr/", "https://www.milesbeckler.com/products-products-product-secret-successful-marketing-answer/"]}, {"email": "tatiotir@itkamer.com", "url": ["https://sfe3be30db12270da.jimcontent.com/download/version/1418461265/module/10869433089/name/Wanda%20POS%20User%20Guide.pdf", "https://sourceforge.net/projects/tatiotir/files/iDempiere/SetupScript/"]}, {"LastpageNbr": 100}, {"canSearch": false}]
        JsonStructure.getFiveFirstEmail(JsonStructure,filecontent,data)