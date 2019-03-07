
from django.test import TestCase
from ..Email import Email

# Create your tests here.
class TestGetEmail(TestCase):

    def testWentAllIsFound(self):
        TestAllEmail = []

        email = Email.getEmail(Email,urls,pureUrl)

        for i in range(len(email)):
            TestAllEmail.append(email[i]['email'])
        self.assertEqual(len(TestAllEmail), 4)
        print(TestAllEmail)
        print("Wow all Emails have been found on the URL you entered !!!")













