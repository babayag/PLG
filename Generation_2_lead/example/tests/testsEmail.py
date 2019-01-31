
from django.test import TestCase
from ..Email import Email

# Create your tests here.
class TestGetEmail(TestCase):

    def testWentAllIsFound(self):
        TestAllEmail = []
        Email.__init__(Email)
        email = Email.getEmail(Email,"itkamer.com")

        for i in range(len(email)):
            TestAllEmail.append(email[i]['email'])
        self.assertEqual(len(TestAllEmail), 4)
        print(TestAllEmail)
        print("Wow all Emails have been found on the URL you entered !!!")




    def testWhenThereIsNullEmailreturn(self):
        TestNullEmail = []
        Email.__init__(Email)
        email = Email.getEmail(Email, "hunter.io")
        for i in range(len(email)):
            TestNullEmail.append(email[i]['email'])
        self.assertEqual(len(TestNullEmail), 0)
        print(TestNullEmail)
        print("Not Emails have not been found on the URL you entered !!")


