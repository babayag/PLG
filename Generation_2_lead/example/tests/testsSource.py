
from django.test import TestCase
from ..Source import Source
from ..Email import Email
# Create your tests here.



class SourceTest(TestCase):

    def test_NoSource(self):
        url = None
        Source.__init__(Source)
        result = Source.appendSource(Source, url)
        self.assertEqual(result, "Not")
        print('no source is returned')

    def test_HaveSource(self):
        url = 'www.example.com'
        Source.__init__(Source)
        result = Source.appendSource(Source, url)
        self.assertEqual(result, ['www.example.com'])
        print(str(len(result)) + ' source is returned')

    def test_duplicatesource(self):
        url = 'www.example.com'
        Source.__init__(Source)
        result = Source.appendSource(Source,url)
        self.assertIn('www.example.com',result)

    def test_AllSourceFound(self):
        TestSource = []
        test = []
        Email.__init__(Email)
        table = Email.getEmail(Email, "itkamer.com")
        for i in range(len(table)):
            TestSource.append(table[i]['url'])
            for j in range(len(TestSource[i])):
                test.append(TestSource[i][j])
        print(test)
        self.assertEqual(len(test), 6)
        # print(TestSource)

        print("Wow all Source of Email have been found on the URL you entered !!!")



