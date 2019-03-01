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
                #Browse 500 results and return searchUrl
                url = BingSearch.browse500Pages(BingSearch, goodUrl)
                emailSource = Email.getEmail(Email, url, goodUrl)
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