from .BingSearch import BingSearch
from .JsonStructure import JsonStructure
from .FileManager import FileManager
from .Email import Email
from .PixelsVerifiers import PixelsVerifiers
import json

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
        response = {}
        FileManager.__init__(FileManager)
        nicheAndCityFile = enterNiche+'_'+enterCity
        files = FileManager.verifyIfFileExist2(FileManager, nicheAndCityFile)
        print(files)
        # PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, "leadmehome.io")
        if files != False:
            filesContent = FileManager.readFile2(FileManager, files)
            allDomains = []
            i = 0
            for item in filesContent[0]["Results"]:
                #I create a new object that will look like {Domain:domain, hasFacebookPixel:Boolean, hasGooglePixel:Boolean, Emails:[]}
                newItem = {"Domain":"", "hasFacebookPixel":False, "hasGooglePixel":False, "Emails":[]}   
                newItem["Domain"] = item["Domain"]
                newItem["Emails"] = item["Emails"]
                hasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, item["Domain"])
                hasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, item["Domain"])
                newItem["hasFacebookPixel"] = hasFaceBookPixel
                newItem["hasGooglePixel"] = hasGooglePixel
                allDomains.append(newItem)
                i=i+1 
            response["Results"] = allDomains
            print(response)
            return response
        else:
            return []
