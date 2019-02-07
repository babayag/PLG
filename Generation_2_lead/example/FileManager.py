
import os
import json
from .BingSearch import BingSearch

class FileManager():

    def WriteInFile(self,data,enterUrl,LastpageNbr):
        os.chdir(r'E:\paness IIHT\M2\project\Nouveau dossier\PLG\jsonFile')
        if self.verifyIfFileExist(self,enterUrl):
            with open("{}.json".format(enterUrl), 'a+') as outfile:
                outfile.seek(0, 2)
                outfile.truncate()
                data.append({"LastpageNbr": LastpageNbr})
                json.dump(data, outfile)

        else:
            try:
                with open("{}.json".format(enterUrl), 'w') as outfile:
                    data.append({"LastpageNbr": LastpageNbr})
                    json.dump(data, outfile)
            except FileNotFoundError:
                pass


    def GetLastPageNumber(self, enterUrl):
        os.chdir(r'E:\paness IIHT\M2\project\Nouveau dossier\PLG\jsonFile')
        try:

            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-1]['LastpageNbr']

        except FileNotFoundError:
            return None

        return lastNumber

    def verifyIfFileExist(self,enterUrl):

        os.chdir(r'E:\paness IIHT\M2\project\Nouveau dossier\PLG\jsonFile')
        if os.path.isfile("{}.json".format(enterUrl)):
            return True
        else:
            return False

