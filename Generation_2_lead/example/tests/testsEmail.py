import re
from django.test import TestCase
from ..Email import Email
from ..FileManager import FileManager
from ..BingSearch import BingSearch
# Create your tests here.
class TestGetEmail(TestCase):



    # test getEmail method

    def testgetEmail(self):
        pageurlsfirst = [[
            "/search?q=%40itkamer.com&first=1",
            "/search?q=%40itkamer.com&first=11",
            "/search?q=%40itkamer.com&first=21",
            "/search?q=%40itkamer.com&first=31",
            "/search?q=%40itkamer.com&first=41",
            "/search?q=%40itkamer.com&first=50"
        ], 1
        ]

        Email.__init__(Email)
        email = Email.getEmail(Email, pageurlsfirst, "itkamer.com")
        self.assertEqual(email, False)

    #test  source is valid or invalid

    def testMain(self):
        enterUrl = "football.com"
        Email.__init__(Email)
        finalData = "YOU ENTERED A GOOD URL!!"
        result = Email.main(Email, enterUrl)
        self.assertEquals(result, finalData)

    #test went all found

    def testWentAllIsFound(self):
        testurl = 'itkamer.com'
        TestAllEmail = []
        FileManager.__init__(FileManager)
        result = FileManager.getFiveFirstEmail(self,testurl)
        for i in range(len(result)-1):
            TestAllEmail.append(result[i]["email"])
        self.assertEqual(len(TestAllEmail), 4)
        print(TestAllEmail)
        print("Wow all Emails have been found on the URL you entered !!!")

#test when there is null email return

    def testWhenThereIsNullEmailreturn(self):
        testurl = 'hunter.io'
        TestNullEmail = []
        FileManager.__init__(FileManager)
        result = FileManager.getFiveFirstEmail(self, testurl)
        for i in range(len(result)-1):
            TestNullEmail.append(result[i]["email"])
        self.assertEqual(len(TestNullEmail), 0)
        print(TestNullEmail)
        print(" Emails have not been found on the URL you entered !!")



#test went has duplicate

    def testHasDuplicates(self):
        bool = False
        testurl = 'itkamer.com'
        FileManager.__init__(FileManager)
        result = FileManager.getFiveFirstEmail(self, testurl)
        for i in range(len(result) - 1):
            for x in range(i + 1, len(result)-1):
                if result[i]["email"] == result[x]["email"]:
                    bool = True
        self.assertEqual(bool, True)

    #test  method  returnTenEmails

 




