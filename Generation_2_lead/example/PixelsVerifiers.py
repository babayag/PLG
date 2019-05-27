import requests
from bs4 import BeautifulSoup

class PixelsVerifiers():
    """
    author : Junior Nouboussi
    params : website
    description : return true if the website has a pixel facebook and false if not
    """
    def VerifyFacebookPixel(self, website):

        req = requests.get("http://"+website)

        soup = BeautifulSoup(req.content, "lxml")
        html = soup.prettify()
        result = html.find('Facebook Pixel') 
        if(result == -1):
           return False

        else:
            return True

#Complete the elements for google analytics search
    """
    author : Junior Nouboussi
    params : website
    description : return true if the website has a google analytics and false if not
    """
    def VerifyGooglePixel(self, website):

        req = requests.get("http://"+website)

        soup = BeautifulSoup(req.content, "lxml")
        html = soup.prettify()
        result = html.find('ga.js')
        result1 = html.find('gtag.js')
        result2 = html.find('analytics.js') 
        if(result != -1) or (result1 != -1) or (result2 != -1):
           return True      

        else:
            return False

    

    
