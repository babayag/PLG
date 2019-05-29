from .BingSearch import BingSearch
from .JsonStructure import JsonStructure
from .FileManager import FileManager
from .Email import Email
from .PixelsVerifiers import PixelsVerifiers
import json

class FindLeads():
    """
    author : Essongo Joel Stephane
    params : EnterNiche , EnterCity 
    description : verify if the file exist for a domain Search     
    """
    def finder(self, enterNiche, enterCity):
        FileManager.__init__(FileManager)
        enterNicheEnterCity = enterNiche+'_'+enterCity
        if FileManager.VerifyIfFileExist(FileManager, enterNicheEnterCity) == True:
            # File exist
            fc = FileManager.ReadFile(FileManager, enterNicheEnterCity)
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

    """
    author : Essongo Joel Stephane, kevin Ngaleu , junior Nouboussi
    params : EnterNiche, EnterCity , p
    description : return list of emails according to a niche and city 
    """
    def findLead(self, enterNiche, enterCity, p):
        response = {}
        FileManager.__init__(FileManager)
        nicheAndCityFile = enterNiche+'_'+enterCity
        files = FileManager.VerifyIfFileExist2(FileManager, nicheAndCityFile)
        print(files)
    
        if files != False:
            filesContent = FileManager.ReadFile2(FileManager, files)
            allDomains = []
            i = 0
            
            if len(filesContent[0]["Results"]) < 10:
                print(len(filesContent[0]["Results"]))
                for item in filesContent[0]["Results"]:
                    #I create a new object that will look like {Domain:domain, hasFacebookPixel:Boolean, hasGooglePixel:Boolean, Emails:[]}
                    newItem = {}   
                    newItem["Domain"] = item["Domain"]
                    newItem["Emails"] = item["Emails"]
                    #hasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, item["Domain"])
                    #hasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, item["Domain"])
                    newItem["hasFacebookPixel"] = "pending"
                    newItem["hasGooglePixel"] = "pending"
                    allDomains.append(newItem)
                    i=i+1 
                response["Results"] = allDomains
                print(response)
                return response
            else:
                if len(filesContent[0]["Results"]) - p >= 10:
                    for p in range(p, p+10): 
                        #I create a new object that will look like {Domain:domain, hasFacebookPixel:Boolean, hasGooglePixel:Boolean, Emails:[]}
                        newItem = {}   
                        item = filesContent[0]["Results"][p]
                        newItem["Domain"] = item["Domain"]
                        newItem["Emails"] = item["Emails"]
                        #hasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, item["Domain"])
                        #hasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, item["Domain"])
                        newItem["hasFacebookPixel"] = "pending"
                        newItem["hasGooglePixel"] = "pending"
                        allDomains.append(newItem)
                        
                    response["Results"] = allDomains
                    print(response)
                    return response
                else:
                    for p in range(p, len(filesContent[0]["Results"])): 
                        #I create a new object that will look like {Domain:domain, hasFacebookPixel:Boolean, hasGooglePixel:Boolean, Emails:[]}
                        newItem = {}   
                        item = filesContent[0]["Results"][p]
                        newItem["Domain"] = item["Domain"]
                        newItem["Emails"] = item["Emails"]
                        #hasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, item["Domain"])
                        #hasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, item["Domain"])
                        newItem["hasFacebookPixel"] = "pending"
                        newItem["hasGooglePixel"] = "pending"
                        allDomains.append(newItem)
                        
                    response["Results"] = allDomains
                    print(response)
                    return response
        else:
            return []


    """
    author : Junioir Nouboussi, Essongo Joel Stephane
    params : domain
    description : verify on a domain if we have pixel or google analytics 
    """
    def checkPixel(self, domain):
        # I create a new item that will look like {hasFacebookPixel:Boolean, hasGooglePixel:Boolean}
        newItem = {} 
        hasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, domain)
        hasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, domain)
        newItem["hasFacebookPixel"] = hasFaceBookPixel
        newItem["hasGooglePixel"] = hasGooglePixel

        return newItem


                        

