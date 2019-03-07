import re
from django.test import TestCase
from ..NicheAndCity import NicheAndCity

class TestNicheAndCity(TestCase):
    def testEmailsByNicheAndCity(self):
        enterNiche = "chiropractor"
        enterCity = "newport"
        actualResult = NicheAndCity.emailsByNicheAndCity(NicheAndCity, enterNiche, enterCity)
        espectResult = False
        self.assertEqual(actualResult, espectResult)