from bs4 import BeautifulSoup

class Source():
    def __init__(self):
        self.sources = []


    """
    author : Essongo Joel Stephane
    params :  li_number, lipath
    description : search a source for the particular email
    return:an object source
    """
    def search(self, li_number, lipath):
        apath = lipath[li_number].findNext("h2").find("a", href=True)
        source = apath["href"]
        return source

    """
    author : Essongo Joel Stephane
    params :  source
    description : add a source to the same email
    return: an object empty or an object source
    """
    def AppendSource(self, source):
        print('dans l object source')
        print(source)
        if type(source) != type('git example'):
           empty = 'Not'
           return empty
        else:
           self.sources.append(source)
           return self.sources
