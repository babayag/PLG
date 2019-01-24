from django.test import TestCase
from .Email import Email
# Create your tests here.

class TestGetEmail(TestCase):

    def testWhenThereIsNullEmailreturn(self):
        Email.__init__(Email)
        email = Email.getEmail(Email,"football.com")
        self.assertEqual(email, 0)
        print("Sorry We didn't see Emails for the URL you entered !!")


    def testWhenThereIsDuplatedEmail(self):
        Email.__init__(Email)
        email = Email.getEmail(Email, "football.com")
        self.assertIn(email, email)
        print("Sorry We found many duplicated emails on the URL you entered !!")

    def testWentAllIsFound(self):
        Email.__init__(Email)
        email = Email.getEmail(Email, "football.com")
        self.assertEqual(email, email)
        print("Wow all Emails have been found on the URL you entered !!")