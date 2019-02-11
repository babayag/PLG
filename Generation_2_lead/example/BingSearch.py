import http.client
import socket
import re


class BingSearch():

    def UrlValidation(self,myUrl):

        regex = re.compile(
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if (re.match(regex, myUrl) is not None ):

            return True
        else:
           return False


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

        myUrl = "/search?q=%40{}&first=11".format(enterUrl)
        result = self.initialSearch(myUrl)
        """try:
            soup = BeautifulSoup(result, features="html.parser")
            txt = soup.find("span", {"class": "sb_count"}).text
            txt = txt.split(" ")[-2]

            try:
                txt = int(txt)
            except:
                txt = txt.split(",")
                txt1 = ""
                for i in range(0, len(txt)):
                    txt1 = txt1 + txt[i]
                txt = int(txt)
        except:
            txt = 101

        if nbrOfLastPage < 100:
            for nbrOfPage in range(1, txt, 10):
                liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage))
                dif = txt - nbrOfPage
                if dif <= 10:
                    liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage + dif))
                    lastN = nbrOfPage + dif
        else:"""

        if nbrOfLastPage != None:

            for nbrOfPage in range(1+nbrOfLastPage, nbrOfLastPage + 50, 10):
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

