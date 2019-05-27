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
    def finder(self, EnterNiche, EnterCity):
        FileManager.__init__(FileManager)
        NicheAndCity = EnterNiche+'_'+EnterCity
        if FileManager.VerifyIfFileExist(FileManager, NicheAndCity) == True:
            # File exist
            fc = FileManager.readFile(FileManager, NicheAndCity)
            EmailToReturn = []
            for domain in fc[-1]['Domain']:
                if BingSearch.UrlValidation(BingSearch,domain):
                    GoodDomain = BingSearch.ExtractGoodDomain(BingSearch,domain)
                    urls = BingSearch.nbrPage(BingSearch, GoodDomain, None, 50)
                    EmailsAndSources = Email.GetEmail(Email, urls, GoodDomain)
                    e = JsonStructure.StructureMultipleDomains(JsonStructure, EmailsAndSources[0], EmailsAndSources[1], GoodDomain)
                    EmailToReturn.append(e)
            print(e)
            return EmailToReturn
        else:
            return False

    """
    author : Essongo Joel Stephane, kevin Ngaleu , junior Nouboussi
    params : EnterNiche, EnterCity , p
    description : return list of emails according to a niche and city 
    """
    def FindLead(self, EnterNiche, EnterCity, p):
        response = {}
        FileManager.__init__(FileManager)
        nicheAndCityFile = EnterNiche+'_'+EnterCity
        files = FileManager.VerifyIfFileExist2(FileManager, nicheAndCityFile)
        print(files)
    
        if files != False:
            FilesContent = FileManager.ReadFile2(FileManager, files)
            AllDomains = []
            i = 0
            
            if len(FilesContent[0]["Results"]) < 10:
                print(len(FilesContent[0]["Results"]))
                for item in FilesContent[0]["Results"]:
                    #I create a new object that will look like {Domain:domain, hasFacebookPixel:Boolean, HasGooglePixel:Boolean, Emails:[]}
                    NewItem = {}   
                    NewItem["Domain"] = item["Domain"]
                    NewItem["Emails"] = item["Emails"]
                    #HasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, item["Domain"])
                    #HasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, item["Domain"])
                    NewItem["hasFacebookPixel"] = "pending"
                    NewItem["HasGooglePixel"] = "pending"
                    AllDomains.append(NewItem)
                    i=i+1 
                response["Results"] = AllDomains
                print(response)
                return response
            else:
                if len(FilesContent[0]["Results"]) - p >= 10:
                    for p in range(p, p+10): 
                        #I create a new object that will look like {Domain:domain, hasFacebookPixel:Boolean, HasGooglePixel:Boolean, Emails:[]}
                        NewItem = {}   
                        item = FilesContent[0]["Results"][p]
                        NewItem["Domain"] = item["Domain"]
                        NewItem["Emails"] = item["Emails"]
                        #HasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, item["Domain"])
                        #HasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, item["Domain"])
                        NewItem["hasFacebookPixel"] = "pending"
                        NewItem["HasGooglePixel"] = "pending"
                        AllDomains.append(NewItem)
                        
                    response["Results"] = AllDomains
                    print(response)
                    return response
                else:
                    for p in range(p, len(FilesContent[0]["Results"])): 
                        #I create a new object that will look like {Domain:domain, hasFacebookPixel:Boolean, HasGooglePixel:Boolean, Emails:[]}
                        NewItem = {}   
                        item = FilesContent[0]["Results"][p]
                        NewItem["Domain"] = item["Domain"]
                        NewItem["Emails"] = item["Emails"]
                        #HasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, item["Domain"])
                        #HasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, item["Domain"])
                        NewItem["hasFacebookPixel"] = "pending"
                        NewItem["HasGooglePixel"] = "pending"
                        AllDomains.append(NewItem)
                        
                    response["Results"] = AllDomains
                    print(response)
                    return response
        else:
            return []

    """
    author : Junioir Nouboussi, Essongo Joel Stephane
    params : domain
    description : verify on a domain if we have pixel or google analytics 
    """
    def CheckPixel(self, domain):
        # I create a new item that will look like {hasFacebookPixel:Boolean, HasGooglePixel:Boolean}
        NewItem = {} 
        HasFaceBookPixel = PixelsVerifiers.VerifyFacebookPixel(PixelsVerifiers, domain)
        HasGooglePixel = PixelsVerifiers.VerifyGooglePixel(PixelsVerifiers, domain)
        NewItem["hasFacebookPixel"] = HasFaceBookPixel
        NewItem["HasGooglePixel"] = HasGooglePixel

        return NewItem


                        

