import re

from django.test import TestCase

from ..JsonStructure import JsonStructure


# Create your tests here.


class Test(TestCase):


   def test_JsonStructure(self):


       #one email one source
       email1 = ["contact@paness-iiht.com"]
       source1 = ["https://docs.google.com"]
       finalData1 = [{'email': 'contact@paness-iiht.com', 'url': ['https://docs.google.com']}]

       result = JsonStructure.JsonStructureReturn(JsonStructure, email1, source1)
       self.assertEquals(result, finalData1)
       print("test1--------------------------------------------------------------------------------------------")
       # no email no source
       email2 = []
       source2 = []
       finalData2 = []

       result = JsonStructure.JsonStructureReturn(JsonStructure, email2, source2)
       self.assertEquals(result, finalData2)
       print("test2--------------------------------------------------------------------------------------------")

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