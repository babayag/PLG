import http.client
import socket
import re
import urllib
from urllib.parse import urlparse
class BingSearch():


    """
    author : ????????
    params : MyUrl
    description : tell if url is good or no good and validate
    return a boolean which tell if the url is good or not good

    """
    def UrlValidation(self,MyUrl):

        regex = re.compile(
            r'^(?:http|ftp)s?://|'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if (re.match(regex, MyUrl) is not None ):
            return True
        else:
           return False

    """
    author : ????????
    params : EnterUrl
    description :  extract a good domain when we enter an url)
    return the good domain
    """

    def ExtractGoodDomain(self, EnterUrl):

        if "http://" in EnterUrl:
            url = EnterUrl[len("http://"):len(EnterUrl)]
            if "www." in url:
                return  url[len("www."):len(url)]
            else:
                return url
        elif "https://" in EnterUrl:
            url = EnterUrl[len("https://"):len(EnterUrl)]
            if "www." in url:
                return  url[len("www."):len(url)]
            else:
                return url
        elif "www." in EnterUrl:
            return EnterUrl[len("www."):len(EnterUrl)]
        else:
            return EnterUrl

    """
    author : ????????
    params : MyUrl
    description :  show a initial url search 
    return the iitial url search
    """
    def InitialSearch(MyUrl):

        # get_Page
        try:
            # always set a timeout when you connect to an external server
            url = "www.bing.com"
            connection = http.client.HTTPSConnection(url, timeout=10)

            connection.request("GET", MyUrl)

            response = connection.getresponse()

            return response.read()
        except socket.timeout:
            # in a real world scenario you would probably do stuff if the
            # socket goes into timeout
            pass

    """
    author : ????????
    params : MyUrl
    description :  show a initial url search 
    return the iitial url search
    """
    def NbrPage(self, EnterUrl,nbrOfLastPage,NbrResultToBrowse):
        liste = []
        lastN = 0

        MyUrl = "/search?q=%40{}&first=11".format(EnterUrl)
        result = self.InitialSearch(MyUrl)
        if nbrOfLastPage != None:
            for nbrOfPage in range(1+nbrOfLastPage, (nbrOfLastPage + NbrResultToBrowse), 10):
                liste.append("/search?q=%40{}&first={}".format(EnterUrl, nbrOfPage))

                dif = int(nbrOfLastPage + NbrResultToBrowse) - nbrOfPage
                if dif <= 10:
                    liste.append("/search?q=%40{}&first={}".format(EnterUrl, nbrOfPage + dif))
                    lastN = nbrOfPage + dif
        else:
            for nbrOfPage in range(1, NbrResultToBrowse, 10):
                liste.append("/search?q=%40{}&first={}".format(EnterUrl, nbrOfPage))
                dif = NbrResultToBrowse - nbrOfPage
                if dif <= 10:
                    liste.append("/search?q=%40{}&first={}".format(EnterUrl, nbrOfPage + dif))
                    lastN = nbrOfPage + dif
        Data = [liste, lastN]
        return Data



