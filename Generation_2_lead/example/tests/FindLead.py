import re
from PLG.Generation_2_lead.example.BingSearch import BingSearch
from PLG.Generation_2_lead.example.JsonStructure import JsonStructure
from PLG.Generation_2_lead.example.FileManager import FileManager
from PLG.Generation_2_lead.example.Email import Email

class FindLeads():
    def cityAndNiche(self, enterNiche, enterCity):
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
                    emailsAndSources = self.getEmail(self, urls, goodDomain)
                    e = JsonStructure.StructureMultipleDomains(JsonStructure, emailsAndSources[0], emailsAndSources[1], goodDomain)
                    emailToReturn.append(e)
            print(e)
            return emailToReturn
        else:
            return False