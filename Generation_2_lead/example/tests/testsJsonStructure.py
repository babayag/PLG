import re

from django.test import TestCase

from ..JsonStructure import JsonStructure


# Create your tests here.


class Test(TestCase):


   def test_JsonStructure(self):
       email1 = ["contact@paness-iiht.com"]
       source1 = ["https://docs.google.com"]
       enterUrl1 = "paness-iiht.com"
       lastPageNumber1 = 50
       #finalData1 = [{'email': 'contact@paness-iiht.com', 'url': ['https://docs.google.com']}]
       finalData1 = False

       result = JsonStructure.JsonStructureReturn(JsonStructure, email1, source1, enterUrl1, lastPageNumber1)
       self.assertEquals(result, finalData1)
       

       """
       #one email one source
       email1 = ["contact@paness-iiht.com"]
       source1 = ["https://docs.google.com"]
       enterUrl1 = "paness-iiht.com"
       lastPageNumber1 = 6
       finalData1 = [{'email': 'contact@paness-iiht.com', 'url': ['https://docs.google.com']}]
       #finalData1 = True

       result = JsonStructure.JsonStructureReturn(JsonStructure, email1, source1,enterUrl1,lastPageNumber1)
       self.assertEquals(result, finalData1)
       print("test1")

       # no email no source
       email2 = []
       source2 = []
       finalData2 = []
       enterUrl2 = "paness-iiht.com"
       lastPageNumber2 = 6
       
       result = JsonStructure.JsonStructureReturn(JsonStructure, email2, source2,enterUrl2,lastPageNumber2)
       self.assertEquals(result, finalData2)
       print("test2")


       # many differents emails and sources

       email3 = ["Isidore@itkamer.com", "isidore@itkamer.com", "sales@itkamer.com", "tatiotir@itkamer.com"]
       source3 = ["https://docs.google.com", "https://stackoverflow.com", "https://github.com",
                  "https://realpython.com"]

       finalData3 = [
           {'email': 'Isidore@itkamer.com', 'url': ['https://docs.google.com']},
           {'email': 'isidore@itkamer.com', 'url': ['https://stackoverflow.com']},
           {'email': 'sales@itkamer.com', 'url': ['https://github.com']},
           {'email': 'tatiotir@itkamer.com', 'url': ['https://realpython.com']},
       ]

       result = JsonStructure.JsonStructureReturn(JsonStructure, email3, source3)
       self.assertEquals(result, finalData3)
       print("test3--------------------------------------------------------------------------------------------")

       # sames emails

       email4 = ["Isidore@itkamer.com", "Isidore@itkamer.com", "Isidore@itkamer.com", "Isidore@itkamer.com", ]
       source4 = ["https://docs.google.com", "https://docs.google.com", "", ""]

       finalData4 = [
           {'email': 'Isidore@itkamer.com', 'url': ['https://docs.google.com']}
       ]

       result = JsonStructure.JsonStructureReturn(JsonStructure, email4, source4)
       self.assertEquals(result, finalData4)
       print("test4--------------------------------------------------------------------------------------------")
       
       source1 = ["https://cameroun.minajobs.net/emplois-stage-recrutement/4635", "https://cameroun.minajobs.net/emplois-stage-recrutement/4635/avis-de-recrutement-dun-agent-dentretien-%e2%80%93-coursier-paness-%e2%80%93-iiht-centre-d%e2%80%99excellence-numerique-at-paness-cabinet-de-conseil-formation-cameroun"]

       """

    def test_getFiveFirstEmail(self):
