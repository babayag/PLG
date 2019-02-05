

from bs4 import BeautifulSoup

class Source():
    def __init__(self):
        self.sources = []


    def search(self, li_number, lipath):
        apath = lipath[li_number].findNext("h2").find("a", href=True)
        source = apath["href"]
        return source


    def appendSource(self, source):
        self.sources.append(source)
        return self.sources
