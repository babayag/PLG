
from django.test import TestCase
from ..Source import Source
from ..Email import Email
# Create your tests here.



class SourceTest(TestCase):

#method test no source
    def test_NoSource(self):
        url = None
        Source.__init__(Source)
        result = Source.appendSource(Source, url)
        self.assertEqual(result, "Not")
        print('no source is returned')
#method test if have source

    def test_HaveSource(self):
        url = 'www.itkamer.com'
        Source.__init__(Source)
        result = Source.appendSource(Source, url)
        self.assertEqual(result, ['www.itkamer.com'])
        print(str(len(result)) + ' source is returned')

#method test if duplicate source

    def test_duplicatesource(self):
        url = 'www.itkamer.com'
        Source.__init__(Source)
        result = Source.appendSource(Source, url)
        self.assertIn('www.itkamer.com', result)
        print('duplicate source')


