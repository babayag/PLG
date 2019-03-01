

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
                        #impossible to find new emails on bing
                        emailsToReturn[2] = False # remove the button see more of the view

                        return emailsToReturn
                    else:
                        #possible to find new emails on bing
                        #print("possible to find new emails on bing 2")
                        urls = BingSearch.nbrPage(BingSearch, pureUrl, nbrPage)
                        scrapedEmail = Email.getEmail(Email, urls,pureUrl)
                        if scrapedEmail == False:
                            # file has been not updated
                            #print("file has been not updated")
                            emailsToReturn[2] = False # remove the button see more of the view
                            return  emailsToReturn
                        else:
                            # file has been updated
                            FileManager.__init__(FileManager)
                            fc = FileManager.readFile(FileManager, pureUrl)
                            emailsToReturn = self.returnTenEmails(self, p, fc)
                            return emailsToReturn
            else: 
                # File does not exist
                
                urls = BingSearch.nbrPage(BingSearch, pureUrl, None)
                scrapedEmail = Email.getEmail(Email, urls,pureUrl)
                if scrapedEmail == True:
                    FileManager.__init__(FileManager)
                    fc = FileManager.readFile(FileManager, pureUrl)
                    emailsToReturn = self.returnTenEmails(self, p, fc)
                    return emailsToReturn
                else:
                    print(5)
                    return []
        else:
            # URL is not valid
            return 'YOU ENTERED A BAD URL!! please enter a url like itkamer.com or wwww.itkamer.com or https://themiddlefingerproject.org'

    def getEmail(self, urls,pureUrl):
        emails = []
        sources = []
        dataToReturn = []
        Source.__init__(Source)
        with PoolExecutor(max_workers=7) as executor:
            print("Workers")
            if type(urls[0]) != str:
                for _ in executor.map(BingSearch.initialSearch, urls[0]):
                    soup = BeautifulSoup(_, features="html.parser")
                    lipath = soup.findAll("li", {"class": "b_algo"})
                    li_number = 0
                    while True:
                        try:
                            litext = lipath[li_number].text
                            # for line in the drivertextclear
                            for line in litext.splitlines():
                                # search all email in each line, return the objet searchNumbers of type list

                                searchEmails = re.findall(r"[a-zA-Z]+[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(pureUrl), line,flags=re.MULTILINE)
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

                datasStructured = JsonStructure.JsonStructureReturn(JsonStructure, emails, sources, pureUrl, urls[1])
                print(datasStructured)
                return datasStructured

            else:

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
                                        #print(emails)
                                        sources = Source.appendSource(Source, src)
                            li_number = li_number + 1

                        except:
                            break

                emailsAndSources =[emails, sources]

                return emailsAndSources