
from django.test import TestCase
from ..Source import Source
from ..Email import Email
# Create your tests here.



class SourceTest(TestCase):


        #method test search
    def test_Search(self):
        url = ["www.itkamer.com","www.example.com"]
        Source.__init__(Source)
        result = Source.search(Source, 1, url)
        print(result)
