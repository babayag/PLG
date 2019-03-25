from .BingSearch import BingSearch
from .JsonStructure import JsonStructure
from .FileManager import FileManager
from .Email import Email

class FindLeads():

    def finder(self, enterNiche, enterCity):
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
                    emailsAndSources = Email.getEmail(Email, urls, goodDomain)
                    e = JsonStructure.StructureMultipleDomains(JsonStructure, emailsAndSources[0], emailsAndSources[1], goodDomain)
                    emailToReturn.append(e)
            print(e)
            return emailToReturn
        else:
            return False

    def findLead(self, enterNiche, enterCity):
        FileManager.__init__(FileManager)
        nicheAndCityFile = enterNiche+'_'+enterCity
        files = FileManager.verifyIfFileExist2(FileManager, nicheAndCityFile)
        if files != False:
            f = FileManager.readFile2(FileManager, files)
            return f
        else:
            return []
