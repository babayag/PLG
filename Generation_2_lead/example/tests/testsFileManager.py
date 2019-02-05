from django.test import TestCase
from ..FileManager import FileManager

# Create your tests here.


class Test(TestCase):

    """
   def test_WriteInFile(self):
    data = [{'email': 'contact@paness-iiht.com', 'url': ['https://docs.google.com']}]
    enterUrl = "itkamer.com"
    LastpageNbr = 1
    finalData1 = True

    result = FileManager.WriteInFile(FileManager, data, enterUrl,LastpageNbr)
    self.assertEquals(result, finalData1)
    #print("test_WriteInFile-----------------------------------------------------------------------------------------")
    """

    """
    def test_GetLastPageNumber(self):
       enterUrl = "cr7.com"
       finalData2 = 21

       result = FileManager.GetLastPageNumber(FileManager,enterUrl)
       self.assertEquals(result, finalData2)
      # print("test_GetLastPageNumber-----------------------------------------------------------------------------------------")
    """

    def test_verifyIfFileExist(self):
        enterUrl = "cr7.com"
        finalData3 = True

        result = FileManager.verifyIfFileExist(FileManager, enterUrl)
        self.assertEquals(result, finalData3)
        # print(" test_verifyIfFileExist-----------------------------------------------------------------------------------------")
