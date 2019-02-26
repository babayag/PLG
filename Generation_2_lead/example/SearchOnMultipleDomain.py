from .BingSearch import BingSearch
from .Email import Email
from .JsonStructure import JsonStructure
from .FileManager import FileManager

class SearchOnMultipleDomain():


    def verifyUrlAndSearchEmail(self,domains):
        ResultForAllDomain = []
        page = 500
 
        for i in domains:
            if BingSearch.UrlValidation(BingSearch,i):
                #goodUrl = BingSearch.extractGoodDomain(BingSearch,i)
                FileManager.__init__(FileManager)
                if FileManager.verifyIfFileExist() == True:

                    fileContent = FileManager.readFile(FileManager,i)
                    return fileContent

                else:

                    url = BingSearch.nbrPage(BingSearch,page)
                    EmailSource = Email.getEmail(Email,url,enterUrl)
                    data = JsonStructure.JsonStructureReturn(JsonStructure,EmailSource[0],EmailSource[1],enterUrl)
            else:
                return 'YOU ENTERED A BAD URL ! enter Url like itikamer.com'