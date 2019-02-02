
import os
import json
from .BingSearch import BingSearch

class FileManager():

    def WriteInFile(self,data,enterUrl,LastpageNbr):
        os.chdir(r'C:\Users\Ranyl\Desktop\tets')

        try:
            if lastNumber <= 100:
                with open("{}.json".format(enterUrl), 'w') as outfile:
                    data.append({"LastpageNbr": LastpageNbr})
                    json.dump(data, outfile)
        except FileNotFoundError:
            pass


    def GetLastPageNumber(self, enterUrl):
        os.chdir(r'C:\Users\Ranyl\Desktop\tets')
        try:

            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-1]['LastpageNbr']


        except FileNotFoundError:
            return None

        return lastNumber

    def verifyIfFileExist(self,enterUrl):

        os.chdir(r'C:\Users\Ranyl\Desktop\tets')
        if os.path.isfile("{}.json".format(enterUrl)):
            return True
        else:
            return False

