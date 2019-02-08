import re
from django.test import TestCase
from ..Email import Email
from ..BingSearch import BingSearch
# Create your tests here.
class TestGetEmail(TestCase):

#test when all found email

    def testWentAllIsFound(self):
        TestAllEmail = []
        Email.__init__(Email)
        email = Email.getEmail(Email, "itkamer.com")

        for i in range(len(email)):
            TestAllEmail.append(email[i]['email'])
        self.assertEqual(len(TestAllEmail), 4)
        print(TestAllEmail)
        print("Wow all Emails have been found on the URL you entered !!!")

#test when there is null email return
    def testWhenThereIsNullEmailreturn(self):
        TestNullEmail = []
        Email.__init__(Email)
        email = Email.getEmail(Email, "hunter.io")
        for i in range(len(email)):
            TestNullEmail.append(email[i]['email'])
        self.assertEqual(len(TestNullEmail), 0)
        print(TestNullEmail)
        print(" Emails have not been found on the URL you entered !!")

#test  source is valid or invalid

    def testMain(self):
        enterUrl = "football.com"
        Email.__init__(Email)
        finalData = "YOU ENTERED A GOOD URL!!"
        result = Email.main(Email, enterUrl)
        self.assertEquals(result, finalData)







