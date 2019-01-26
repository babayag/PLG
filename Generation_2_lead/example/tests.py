from django.test import TestCase
from .Source import Source

# Create your tests here.


class YourTestClass(TestCase):
   def test_nosource(self):
       ago = None
       Source.__init__(Source)
       result = Source.appendSource(Source,ago)
       self.assertEqual(result,'Not')

   def test_duplicatesource(self):

       ago = 're'
       before = 're'
       Source.__init__(Source)
       result = Source.appendSource(Source,ago)
       self.assertNotIn(before,result)



