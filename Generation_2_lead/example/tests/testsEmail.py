import re
from django.test import TestCase
from ..Email import Email
from ..FileManager import FileManager
from ..BingSearch import BingSearch
# Create your tests here.
class TestGetEmail(TestCase):

  # test GetEmail method
    """
    author : ??????????????
    params : urls, PureURL
    description : ??????
    return:Emails And Sources
    """
    def testgetEmail(self):
        PageUrlsFirst = ['/search?q=%40forbes.com&first=1', '/search?q=%40forbes.com&first=11', '/search?q=%40forbes.com&first=21', '/search?q=%40forbes.com&first=31', '/search?q=%40forbes.com&first=41', '/search?q=%40forbes.com&first=50']
        expectedResult = ['akonrad@forbes.com', 'corrections@forbes.com', 'readers@forbes.com', 'ideas@forbes.com', 'feedback@forbes.com', 'opinion@forbes.com', 'jtorres@forbes.com', 'unaum@forbes.com', 'corrections@forbes.com', 'opinion@forbes.com', 'opinion@forbes.com', 'mwells@forbes.com', 'opinion@forbes.com', 'Lopenzina@forbes.com', 'atracy@forbes.com', 'opinion@forbes.com', 'research@forbes.com']
        Email.__init__(Email)
        email = Email.GetEmail(Email, PageUrlsFirst, "forbes.com")
        self.assertEqual(len(email[0]), len(expectedResult))

    #test  source is valid or invalid

    """def testMain(self):
        enterUrl = "footballcom"
        nbrEmail = 0
        Email.__init__(Email)
        finalData = "YOU ENTERED A BAD URL!!"
        result = Email.main(Email, enterUrl, nbrEmail)
        self.assertEquals(result, finalData)
    #test went all found"""

#     def testWentAllIsFound(self):
#         testurl = 'itkamer.com'
#         TestAllEmail = []
#         FileManager.__init__(FileManager)
#         result = FileManager.getFiveFirstEmail(FileManager, testurl)
#         for i in range(len(result)-1):
#             TestAllEmail.append(result[i]["email"])
#         self.assertEqual(len(TestAllEmail), 4)
#         print(TestAllEmail)
#         print("Wow all Emails have been found on the URL you entered !!!")

# #test when there is null email return

#     def testWhenThereIsNullEmailreturn(self):
#         testurl = 'hunter.io'
#         TestNullEmail = []
#         FileManager.__init__(FileManager)
#         result = FileManager.getFiveFirstEmail(FileManager, testurl)
#         for i in range(len(result)-1):
#             TestNullEmail.append(result[i]["email"])
#         self.assertEqual(len(TestNullEmail), 0)
#         print(TestNullEmail)
#         print(" Emails have not been found on the URL you entered !!")


#test went has duplicate


    # def testHasDuplicates(self):
    #     bool = False
    #     testurl = 'itkamer.com'
    #     FileManager.__init__(FileManager)
    #     result = FileManager.getFiveFirstEmail(FileManager, testurl)
    #     for i in range(len(result) - 1):
    #         for x in range(i + 1, len(result)-1):
    #             if result[i]["email"] == result[x]["email"]:
    #                 bool = True
    #     self.assertEqual(bool, True)

    #test  method  returnTenEmails

    # def testreturnTenEmails(self):
    #     enterUrl = ["kerrycfan@football.com",
    #                 "koh@football.com",
    #                 "joe@football.com",
    #                 "info@football.com",
    #                 "ralph@football.com",
    #                 "dasilva@football.com",
    #                 "joegibbs@football.com",
    #                 "texas@football.com",
    #                 "pb@football.com",
    #                 "association@football.com",
    #                 "botchtotebag@football.com",
    #                 "tich-tiraline-amour@football.com"]

    #     nbrEmail = 0
    #     Email.__init__(Email)
    #     result = Email.returnTenEmails(Email, nbrEmail, enterUrl)
    #     resulttest = 10
    #     print(result[1])
    #     self.assertEquals(result[1], resulttest)

    # def testDownloadEmails(self):
    #     url = "https://www.itkamer.com"
    #     Email.__init__(Email)
    #     result = Email.DownloadEmails(Email,url)
    #     self.assertEqual(type(len(result)),int)


    """def testFindLeads(self):
        enterNiche = "chiropractor"
        enterCity = "newport"
        actualResult = Email.cityAndNiche(Email, enterNiche, enterCity)
        espectResult = False
        self.assertEqual(actualResult, espectResult)"""



        urls = ["football.com", "itkamer.com"]
        enterUrl = "football"
        #finalData2 = " "

        result = Email.getEmail(Email, urls, enterUrl)
        self.assertEquals(result, finalData2)
