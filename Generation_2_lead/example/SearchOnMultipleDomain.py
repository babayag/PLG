from .BingSearch import BingSearch
from .Email import Email
from .JsonStructure import JsonStructure

class SearchOnMultipleDomain():

    """
    author : Ranyl Foumbi
    params : domains
    description : verify and search emails on multiple domain (bulk search) and return list of emails for each domain 
    """
    def VerifyUrlAndSearchEmail(self,domains):
        DatasStructured = []
        for DomaineName in domains:
            #if Url respect Url Patern
            if BingSearch.UrlValidation(BingSearch,DomaineName) == True:
                #extract good domaine from the enterUrl
                GoodUrl = BingSearch.ExtractGoodDomain(BingSearch,DomaineName)
                #Browse 200 results and return searchUrl and NbrOfLastPage as here we don't use last page we put None
                url = BingSearch.NbrPage(BingSearch,GoodUrl,None,200)
                #url = [listeOfUrl , LastPageNbr] so we need only listeOfUrl it is why we write url[0]
                EmailSource = Email.getEmail(Email, url[0], GoodUrl)
                # EmailSource is an array of Array of Emails and Array of Sources
                #we call JsonStructure to stucture data as we want
                DatasStructured.append(JsonStructure.StructureMultipleDomains(JsonStructure, EmailSource[0], EmailSource[1], GoodUrl))
            else:
                #if url is not valid  return empty table
                DomainEmailAndUrl = {
                    "Domain": DomaineName,
                    # set data list content to concern attribut
                    "concern": []
                }
                DatasStructured.append(DomainEmailAndUrl)
        return DatasStructured
