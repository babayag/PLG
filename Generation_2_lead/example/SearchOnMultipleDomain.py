from .BingSearch import BingSearch
from .Email import Email
from .JsonStructure import JsonStructure

class SearchOnMultipleDomain():


    def verifyUrlAndSearchEmail(self,domains):
        datasStructured = []
        for i in domains:
            #if Url respect Url Patern
            if BingSearch.UrlValidation(BingSearch,i):
                #extract good domaine from the enterUrl
                goodUrl = BingSearch.extractGoodDomain(BingSearch,i)
                #Browse 200 results and return searchUrl and NbrOfLastPage as here we done use last page we put None
                url = BingSearch.nbrPage(BingSearch,goodUrl,None,200)
                #url = [listeOfUrl , LastPageNbr] so we need only listeOfUrl it is why we write url[0]
                emailSource = Email.getEmail(Email, url[0], goodUrl)
                print(emailSource)
                # emailSource is an array of Array of Emails and Array of Sources
                #we call JsonStructure to stucture data as we want
                datasStructured.append(JsonStructure.StructureMultipleDomains(JsonStructure, emailSource[0], emailSource[1], goodUrl))
            else:
                #if url is not valid  return empty table
                DomainEmailAndUrl = {
                    "Domain": i,
                    # set data list content to concern attribut
                    "concern": []
                }
                datasStructured.append(DomainEmailAndUrl)
        return datasStructured