import re
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from bs4 import BeautifulSoup
from .BingSearch import BingSearch
from .Source import Source
from .JsonStructure import JsonStructure
from .FileManager import FileManager

class Email():

    def returnTenEmails(self, p, fileContent):
        result = []
        allEmails = fileContent[0:len(fileContent)-2]
        p = int(p)
        if len(allEmails[p:]) >= 10:
            emailsToReturn = allEmails[p:(p+10)]
            result.append(emailsToReturn)
            p += len(emailsToReturn)
            result.append(p)
            result.append(True)
            return result
        else:
            emailsToReturn = allEmails[p:]
            result.append(emailsToReturn)
            p += len(emailsToReturn)
            result.append(p)
            result.append(True)
            return result

    def DownloadEmails(self, enterUrl):
        if BingSearch.UrlValidation(BingSearch,enterUrl) == True:
            # URL is valid
            pureUrl = BingSearch.extractGoodDomain(BingSearch, enterUrl)
            FileManager.__init__(FileManager)
            if FileManager.verifyIfFileExist(FileManager,pureUrl) == True:
                # File exist in the directory
                FileManager.__init__(FileManager)
                fc = FileManager.readFile(FileManager, pureUrl)
                emailsToReturn = fc[0:len(fc)-2]
                return emailsToReturn
            else:
                return " FILE IS NOT EXIST !!!"
        else:
            return 'YOU ENTERED A BAD URL !!!'

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

    def main(self, enterUrl, p):
        if BingSearch.UrlValidation(BingSearch,enterUrl) == True:
            # URL is valid
            pureUrl = BingSearch.extractGoodDomain(BingSearch, enterUrl)
            FileManager.__init__(FileManager)
            if FileManager.verifyIfFileExist(FileManager, pureUrl) == True:
                # File exist in the directory
                print("File exist in the directory")
                FileManager.__init__(FileManager)
                fc = FileManager.readFile(FileManager, pureUrl)
                nbrPage = FileManager.GetLastPageNumber(FileManager, pureUrl)
                emailsToReturn = self.returnTenEmails(self, p, fc)
                if len(emailsToReturn[0]) == 10:
                    return emailsToReturn
                else:
                    if fc[-1]['canSearch'] == False:
                        print("test 0")
                        #impossible to find new emails on bing
                        emailsToReturn[2] = False # remove the button see more of the view

                        return emailsToReturn
                    else:
                        #possible to find new emails on bing
                        urls = BingSearch.nbrPage(BingSearch, pureUrl, nbrPage,50)
                        scrapedEmail = Email.getEmail(Email, urls,pureUrl)
                        datasStructured = JsonStructure.JsonStructureReturn(JsonStructure, scrapedEmail[0], scrapedEmail[1], pureUrl, urls[1])
                        print(datasStructured)
                        if datasStructured == False:
                            print("test 1")
                            # file has been not updated
                            #print("file has been not updated")
                            emailsToReturn[2] = False # remove the button see more of the view
                            return  emailsToReturn
                        else:
                            print("test 2")
                            # file has been updated
                            FileManager.__init__(FileManager)
                            fc = FileManager.readFile(FileManager, pureUrl)
                            emailsToReturn = self.returnTenEmails(self, p, fc)
                            return emailsToReturn
            else: 
                # File does not exist
                
                urls = BingSearch.nbrPage(BingSearch, pureUrl, None,50)
                scrapedEmail = Email.getEmail(Email, urls,pureUrl)
                datasStructured = JsonStructure.JsonStructureReturn(JsonStructure, scrapedEmail[0], scrapedEmail[1],pureUrl, urls[1])
                if datasStructured == True:
                    FileManager.__init__(FileManager)
                    fc = FileManager.readFile(FileManager, pureUrl)
                    emailsToReturn = self.returnTenEmails(self, p, fc)
                    return emailsToReturn
                else:
                    return []
        else:
            # URL is not valid
            return 'YOU ENTERED A BAD URL!! please enter a url like itkamer.com or wwww.itkamer.com or https://themiddlefingerproject.org'

    

    def getEmail(self, urls,pureUrl):
        emails = []
        sources = []
        Source.__init__(Source)
        with PoolExecutor(max_workers=7) as executor:
            print("Workers")
            if type(urls[0]) == str:
                urls = urls
            else:
                urls = urls[0]

            for _ in executor.map(BingSearch.initialSearch, urls):
                soup = BeautifulSoup(_, features="html.parser")
                lipath = soup.findAll("li", {"class": "b_algo"})
                li_number = 0
                while True:
                    try:
                        litext = lipath[li_number].text
                        # for line in the drivertextclear
                        for line in litext.splitlines():
                            # search all email in each line, return the objet searchNumbers of type list

                            searchEmails = re.findall(r"[a-zA-Z]+[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(pureUrl),
                                                      line, flags=re.MULTILINE)
                            # for email in email_1 list

                            if searchEmails:
                                src = Source.search(Source, li_number, lipath)
                                for email in searchEmails:
                                    # add email in the emails list: return an object oy type NoneType
                                    emails.append(email)
                                    sources = Source.appendSource(Source, src)
                        li_number = li_number + 1

                    except:
                        break
            emailsAndSources = [emails, sources]
            return emailsAndSources
