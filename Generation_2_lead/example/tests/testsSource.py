
from django.test import TestCase
from ..Source import Source
from ..Email import Email
# Create your tests here.



class SourceTest(TestCase):


    # #------------------ method test search ----------------------------------
    # def testSearch(self):
    #     print("---- Test of the method Source.search() -----")
    #     url = ["www.itkamer.com","www.example.com"]
    #     Source.__init__(Source)s
    #     result = Source.search(Source, 1, url)
    #     print(result)


    #------------------ method test appendSource ----------------------------------
    def testAppendSourceWhenNotCorrect(self):
        print("---- Test of the method Source.appendSource() -----")
        print("~~~~~~~ case when a non-str object is entered as Source ~~~~~~~~~")
        source = 45495
        Source.__init__(Source)
        result = Source.appendSource(Source, source)
        print(result)

    def testAppendSourceWhenCorrect(self):
        print("~~~~~~~~~ case when an str object is entered as Source ~~~~~~~~~~~")
        source = "I am a correct str object"
        Source.__init__(Source)
        result = Source.appendSource(Source, source)
        print(result)
