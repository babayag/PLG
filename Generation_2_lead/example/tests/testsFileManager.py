from django.test import TestCase
from ..FileManager import FileManager
import re


    """ 
    author : Sonfack Cindy, Nouboussi junior
    params : data, enterUrl, LastpageNbr, canSearch
    description : test the WriteInFile method (this method  write in a json file (email found, url entered ,the LastpageNbr, and the boolean canSearch))
    return data, enterUrl, LastpageNbr, canSearch and a msg which tell that there's no error in the files
    """
    #----------------------- method test WriteInFile() ------------------------
    def testWriteInFileVoidData(self):
        print("----------Test of the method WriteInFile() -------------------")
        print("~~~~~~~~+ Case when data to write are void ~~~~~~~~~~~~~~")
        enterUrl = 'testvoidurl.com'
        data = []
        lastNbrPage = 0
        canSearch = True
        FileManager.__init__(FileManager)
        FileManager.WriteInFile(FileManager, data, testUrl, lastNbrPage, canSearch)
        print("SUCCESS, No Error in File writing")

    def testWriteInFile(self):
        print("~~~~~~~~+ Case when data to write are a correct object ~~~~~~~~~~~~~~")
        testUrl = 'testurlNormal.com'
        data = [{"email": "bill@cindy.com", "url": ["https://www.csindy.com/coloradosprings/dance-dance-evolution/Content?oid=1146282", "https://www.csindy.com/coloradosprings/guns-and-rabies/Content?oid=1358574"]}, {"email": "cindy@cindy.com", "url": ["http://excel.bigresource.com/Removing-duplicate-entries-from-two-lists--YbA06aaZ.html", "https://it.toolbox.com/question/mail-with-the-subject-and-from-address-032106", "https://www.excelforum.com/excel-general/652943-removing-duplicate-entries-from-two-lists.html"]}, {"email": "filecindy@cindy.com", "url": ["https://www.grandandtoy.com/OnlineRepository/omxDS/PDF/comparison-doc_Part10.pdf"]}, {"email": "htmlinfo@cindy.com", "url": ["http://www.emailbiz.info/view-email-list/Free-email-list-78108/78108.html"]}, {"email": "rosescindy@cindy.com", "url": ["https://katalogus.eoldal.hu/weboldal/92316/guns-n----roses"]}, {"email": "string--jvLJUD9G.htmlcindy@cindy.com", "url": ["http://excel.bigresource.com/Removing-duplicate-in-a-string--jvLJUD9G.html"]}, {"email": "sztar_email4_budai_attila_botondcindy@cindy.com", "url": ["http://www.deathnoteandbleach.sokoldal.hu/sztar_email4_budai_attila_botond"]}, {"email": "sztarok-gyerekkepeicindy@cindy.com", "url": ["http://iskolaujsag.mlap.hu/html/19148612/render/sztarok-gyerekkepei"]}]
        lastNbrPage = 0
        canSearch = True
        FileManager.__init__(FileManager)
        FileManager.WriteInFile(FileManager, data, testUrl, lastNbrPage, canSearch)
        print("SUCCESS, No Error in File writing")

    def testWriteInFileWhenLastNbrIsNotNull(self):
        print("~~~~~~~~+ Case when lestNbrPage is not null ~~~~~~~~~~~~~~")
        testUrl = 'testurlNbrPage.com'
        data = [{"email": "bill@cindy.com", "url": ["https://www.csindy.com/coloradosprings/dance-dance-evolution/Content?oid=1146282", "https://www.csindy.com/coloradosprings/guns-and-rabies/Content?oid=1358574"]}, {"email": "cindy@cindy.com", "url": ["http://excel.bigresource.com/Removing-duplicate-entries-from-two-lists--YbA06aaZ.html", "https://it.toolbox.com/question/mail-with-the-subject-and-from-address-032106", "https://www.excelforum.com/excel-general/652943-removing-duplicate-entries-from-two-lists.html"]}, {"email": "filecindy@cindy.com", "url": ["https://www.grandandtoy.com/OnlineRepository/omxDS/PDF/comparison-doc_Part10.pdf"]}, {"email": "htmlinfo@cindy.com", "url": ["http://www.emailbiz.info/view-email-list/Free-email-list-78108/78108.html"]}, {"email": "rosescindy@cindy.com", "url": ["https://katalogus.eoldal.hu/weboldal/92316/guns-n----roses"]}, {"email": "string--jvLJUD9G.htmlcindy@cindy.com", "url": ["http://excel.bigresource.com/Removing-duplicate-in-a-string--jvLJUD9G.html"]}, {"email": "sztar_email4_budai_attila_botondcindy@cindy.com", "url": ["http://www.deathnoteandbleach.sokoldal.hu/sztar_email4_budai_attila_botond"]}, {"email": "sztarok-gyerekkepeicindy@cindy.com", "url": ["http://iskolaujsag.mlap.hu/html/19148612/render/sztarok-gyerekkepei"]}]
        lastNbrPage = 50
        canSearch = True
        FileManager.__init__(FileManager)
        FileManager.WriteInFile(FileManager, data, testUrl, lastNbrPage, canSearch)
        print("SUCCESS, No Error in File writing")

    """
    author : Sonfack Cindy, Nouboussi junior
    params :EnterUrl
    description : test the GetLastPageNumber method (this method get the last page when we search email on an Enterurl to continue where we stop )
    return lastNumberPage
    """
    #----------------  method test GetLastPageNumber() ---------------------
    def testGestLastNumberWhenNotExists(self):
        print("----------Test of the method GetLastPageNumber() -------------------")
        print("~~~~~~~~+ Case when last Number Page does not exist ~~~~~~~~~~~~~~")
        testUrl = 'idontexist.com'
        FileManager.__init__(FileManager)
        lastPageNumber = FileManager.GetLastPageNumber(FileManager, testUrl)
        if lastPageNumber == None:
            print("no last page number for this url")
        else:
            print("last page number found, it is")
            print(lastPageNumber)

    def testGestLastNumberWhenItExists(self):
        print("~~~~~~~~+ Case when last number of page exists ~~~~~~~~~~~~~~")
        testUrl = 'football.com'
        FileManager.__init__(FileManager)
        lastPageNumber = FileManager.GetLastPageNumber(FileManager, testUrl)
        if lastPageNumber == None:
            print("no last page number for this url")
        else:
            print("last page number found, it is")
            print(lastPageNumber)

    #----------------------- method test VerifyIfFileExist() ----------------------
    
    """
    author : Sonfack Cindy, Nouboussi junior
    params :EnterUrl
    description : test the VerifyIfFileExist method (this method  verify if the file exist for a domain search )
    return a boolean and a msg  which tell if file exist or no 
    """
    def testVerifyIfFileExistsWhenNot(self):
        print("----------Test of the method GetLastPageNumber() -------------------")
        print("~~~~~~~~+ Case when file does not exist ~~~~~~~~~~~~~~")
        file = "idontexist.com"
        FileManager.__init__(FileManager)
        result = FileManager.VerifyIfFileExist(FileManager, file)
        if result == False:
            print("File for url "+ file+" Doesn't Exist")

    def testVerifyIfFileExistsWhenYes(self):
        print("~~~~~~~~+ Case when file exists ~~~~~~~~~~~~~~")
        file = "testurlNormal.com"
        FileManager.__init__(FileManager)
        result = FileManager.VerifyIfFileExist(FileManager, file)
        if result == True:
            print("File for url " + file + " Exists")

    """
    author : Sonfack Cindy, Nouboussi junior
    params : EnterUrl
    description : test a ReadFile method (this method ReadFile for a domain search )
    return FileContent
    """
    # ---------------------------  method test ReadFile() ----------------------------
    def testReadFileContent(self):
        print("----------Test of the method ReadFileContent() -------------------")
        file = "idontexist.com"
        FileManager.__init__(FileManager)
        result = FileManager.ReadFile(FileManager, file)
        print(result)


    #---------------------------- method test ReadFile2() ----------------------------
    def testReadFile2(self):
        print("----------Test of the method testReadFile2() -------------------")
        files = ["itkamer.com", "FFF.com"]
        FileManager.__init__(FileManager)
        result = FileManager.ReadFile2(FileManager, files)
        print(result)

        result = FileManager.WriteInFile(FileManager, data, enterUrl,LastpageNbr,canSearch)
        self.assertEquals(result, finalData1)
    
        
