import re
from .BingSearch import BingSearch
from .JsonStructure import JsonStructure
from .FileManager import FileManager
from .Email import Email

class NicheAndCity():
    def emailsByNicheAndCity(self, enterNiche, enterCity):
        FileManager.__init__(FileManager)
        enterNicheEnterCity = enterNiche+'_'+enterCity
        if FileManager.verifyIfFileExist(FileManager, enterNicheEnterCity) == True:
            # File exist
            fc = FileManager.readFile(FileManager, enterNicheEnterCity)
            emailToReturn = []
            for domain in fc[-1]['Domain']:
                if BingSearch.UrlValidation(BingSearch,domain):
                    goodDomain = BingSearch.extractGoodDomain(BingSearch,domain)
                    urls = BingSearch.nbrPage(BingSearch, goodDomain, None, 50)
                    emailsAndSources = Email.getEmail(self, urls, goodDomain)
                    emailsAndSourcesStructured = JsonStructure.StructureMultipleDomains(JsonStructure, emailsAndSources[0], emailsAndSources[1], goodDomain)
                else:
                    return "This URL is invalid !"
                emailToReturn.append(emailsAndSourcesStructured)
            return emailToReturn
        else:
            return "File is not available !"