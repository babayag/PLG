import http.client
import socket
import re
import urllib
from urllib.parse import urlparse
class BingSearch():

    def UrlValidation(self,myUrl):

        regex = re.compile(
            r'^(?:http|ftp)s?://|'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if (re.match(regex, myUrl) is not None ):
            return True
        else:
           return False

    def extractGoodDomain(self, enterUrl):
        goodDomain = enterUrl
        if "://" in enterUrl:
           splitenterUrl = enterUrl.split("://")
           splitpoint = splitenterUrl[1].split(".")
           if len(splitpoint) > 2:
              splitextension = splitpoint[2].split('/')
              goodDomain = splitpoint[1]+'.'+splitextension[0]
              return goodDomain
           else:
              splitextension = splitpoint[1].split('/')
              goodDomain = splitpoint[0]+'.'+splitextension[0]
              return goodDomain

        elif enterUrl.count('.') > 1:
            
            splitpoint = enterUrl.split(".")
            splitextension = splitpoint[2].split('/')
            goodDomain = splitpoint[1]+'.'+splitextension[0]
            return goodDomain
        elif enterUrl.count('.') == 1:
             splitpoint = enterUrl.split(".")
             splitextension = splitpoint[1].split('/')
             goodDomain = splitpoint[0]+'.'+splitextension[0]
             return goodDomain
        else:
            return goodDomain

    def initialSearch(myUrl):

        # get_Page
        try:
            # always set a timeout when you connect to an external server
            url = "www.bing.com"
            connection = http.client.HTTPSConnection(url, timeout=10)

            connection.request("GET", myUrl)

            response = connection.getresponse()

            return response.read()
        except socket.timeout:
            # in a real world scenario you would probably do stuff if the
            # socket goes into timeout
            pass

    def nbrPage(self, enterUrl,nbrOfLastPage):
        liste = []
        lastN = 0
        print(nbrOfLastPage)

        myUrl = "/search?q=%40{}&first=11".format(enterUrl)
        result = self.initialSearch(myUrl)
        if nbrOfLastPage != None:
            for nbrOfPage in range(1+nbrOfLastPage, (nbrOfLastPage + 50), 10):
                liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage))

                dif = int(nbrOfLastPage + 50) - nbrOfPage
                if dif <= 10:
                    liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage + dif))
                    lastN = nbrOfPage + dif
        else:
            for nbrOfPage in range(1, 50, 10):
                liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage))
                dif = 50 - nbrOfPage
                if dif <= 10:
                    liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage + dif))
                    lastN = nbrOfPage + dif
        data = [liste, lastN]
        return data

