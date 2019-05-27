import re
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from bs4 import BeautifulSoup
from .BingSearch import BingSearch
from .Source import Source
from .JsonStructure import JsonStructure
from .FileManager import FileManager


class Email():
    """
    author : Essongo Joel Stephane
    params : FileContent
    description : give the 10 first emails
    return : 10 emails starting at the p position in the file content
    """
    def ReturnTenEmails(self, p, FileContent):
        result = []
        allEmails = FileContent[0:len(FileContent)-2]
        p = int(p)
        if len(allEmails[p:]) >= 10:
            EmailsToReturn = allEmails[p:(p+10)]
            result.append(EmailsToReturn)
            p += len(EmailsToReturn)
            result.append(p)
            result.append(True)
            return result
        else:
            EmailsToReturn = allEmails[p:]
            result.append(EmailsToReturn)
            p += len(EmailsToReturn)
            result.append(p)
            result.append(True)
            return result

    """
    author : Essongo Joel Stephane
    params : EnterUrl
    description : get the list of emails for when the file for that domain exist
    return:a string msg 
    """
    def DownloadEmails(self, EnterUrl):
        if BingSearch.UrlValidation(BingSearch,EnterUrl) == True:
            # URL is valid
            PureUrl = BingSearch.ExtractGoodDomain(BingSearch, EnterUrl)
            FileManager.__init__(FileManager)
            if FileManager.VerifyIfFileExist(FileManager,PureUrl) == True:
                # File exist in the directory
                FileManager.__init__(FileManager)
                fc = FileManager.ReadFile(FileManager, PureUrl)
                EmailsToReturn = fc[0:len(fc)-2]
                return EmailsToReturn
            else:
                return " FILE IS NOT EXIST !!!"
        else:
            return 'YOU ENTERED A BAD URL !!!'

    """
    author : Essongo Joel Stephane
    params : EnterNiche, EnterCity  
    description : get emails for a nich and a particular location
    return:a json object EmailToReturn (domains,emails) or false
    """
    def CityAndNiche(self, EnterNiche, EnterCity):
        FileManager.__init__(FileManager)
        EnterNicheEnterCity = EnterNiche+'_'+EnterCity
        if FileManager.VerifyIfFileExist(FileManager, EnterNicheEnterCity) == True:
            # File exist
            fc = FileManager.ReadFile(FileManager, EnterNicheEnterCity)
            EmailToReturn = []
            for domain in fc[-1]['Domain']:
                if BingSearch.UrlValidation(BingSearch,domain):
                    GoodDomain = BingSearch.ExtractGoodDomain(BingSearch,domain)
                    urls = BingSearch.NbrPage(BingSearch, GoodDomain, None, 50)
                    EmailsAndSources = self.GetEmail(self, urls, GoodDomain)
                    e = JsonStructure.StructureMultipleDomains(JsonStructure, EmailsAndSources[0], EmailsAndSources[1], GoodDomain)
                    EmailToReturn.append(e)
            print(e)
            return EmailToReturn
        else:
            return False

    """
    author : Essongo Joel Stephane
    params : EnterUrl, p
    description : ask to Essongo 
    return:
    """
    def main(self, EnterUrl, p):
        if BingSearch.UrlValidation(BingSearch,EnterUrl) == True:
            # URL is valid
            PureUrl = BingSearch.ExtractGoodDomain(BingSearch, EnterUrl)
            FileManager.__init__(FileManager)
            if FileManager.VerifyIfFileExist(FileManager, PureUrl) == True:
                # File exist in the directory
                print("File exist in the directory")
                FileManager.__init__(FileManager)
                fc = FileManager.ReadFile(FileManager, PureUrl)
                NbrPage = FileManager.GetLastPageNumber(FileManager, PureUrl)
                EmailsToReturn = self.ReturnTenEmails(self, p, fc)
                if len(EmailsToReturn[0]) == 10:
                    return EmailsToReturn
                else:
                    if fc[-1]['CanSearch'] == False:
                        print("test 0")
                        #impossible to find new emails on bing
                        EmailsToReturn[2] = False # remove the button see more of the view

                        return EmailsToReturn
                    else:
                        #possible to find new emails on bing
                        urls = BingSearch.NbrPage(BingSearch, PureUrl, NbrPage,50)
                        ScrapedEmail = Email.GetEmail(Email, urls,PureUrl)
                        DatasStructured = JsonStructure.JsonStructureReturn(JsonStructure, ScrapedEmail[0], ScrapedEmail[1], PureUrl, urls[1])
                        print(DatasStructured)
                        if DatasStructured == False:
                            # file has been not updated
                            #print("file has been not updated")
                            EmailsToReturn[2] = False # remove the button see more of the view
                            return  EmailsToReturn
                        else:
                            # file has been updated
                            FileManager.__init__(FileManager)
                            fc = FileManager.ReadFile(FileManager, PureUrl)
                            EmailsToReturn = self.ReturnTenEmails(self, p, fc)
                            return EmailsToReturn
            else: 
                # File does not exist
                
                urls = BingSearch.NbrPage(BingSearch, PureUrl, None,50)
                ScrapedEmail = Email.GetEmail(Email, urls,PureUrl)
                DatasStructured = JsonStructure.JsonStructureReturn(JsonStructure, ScrapedEmail[0], ScrapedEmail[1],PureUrl, urls[1])
                if DatasStructured == True:
                    FileManager.__init__(FileManager)
                    fc = FileManager.ReadFile(FileManager, PureUrl)
                    EmailsToReturn = self.ReturnTenEmails(self, p, fc)
                    return EmailsToReturn
                else:
                    return []
        else:
            # URL is not valid
            return 'YOU ENTERED A BAD URL!!'

    
    """
    author : ??????????????
    params : urls, PureURL
    description : ??????
    return:Emails And Sources
    """
    def GetEmail(self, urls,PureUrl):
        emails = []
        sources = []
        Source.__init__(Source)
        with PoolExecutor(max_workers=7) as executor:
            print("Workers")
            if type(urls[0]) == str:
                urls = urls
            else:
                urls = urls[0]

            for _ in executor.map(BingSearch.InitialSearch, urls):
                soup = BeautifulSoup(_, features="html.parser")
                lipath = soup.findAll("li", {"class": "b_algo"})
                li_number = 0
                while True:
                    try:
                        litext = lipath[li_number].text
                        # for line in the drivertextclear
                        for line in litext.splitlines():
                            # search all email in each line, return the objet searchNumbers of type list

                            SearchEmails = re.findall(r"[a-zA-Z]+[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(PureUrl),
                                                      line, flags=re.MULTILINE)
                            # for email in email_1 list

                            if SearchEmails:
                                src = Source.search(Source, li_number, lipath)
                                for email in SearchEmails:
                                    # add email in the emails list: return an object oy type NoneType
                                    emails.append(email)
                                    sources = Source.appendSource(Source, src)
                        li_number = li_number + 1

                    except:
                        break
            print(emails)
            EmailsAndSources = [emails, sources]
            return EmailsAndSources
