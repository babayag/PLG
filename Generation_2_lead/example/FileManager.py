import os
import json
from datetime import datetime
import time

class FileManager():

    def __init__(self):
        self.cacheFolderPath = r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\cache'
        self.leadFolderPath = r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\leads'

    def WriteInFile(self, data, enterUrl, LastpageNbr, canSearch):
        os.chdir(self.cacheFolderPath)
        if self.verifyIfFileExist(self, enterUrl):
            fdata = []
            try:
                with open("{}.json".format(enterUrl), 'r') as outfile:
                    fdata = json.load(outfile)
                    # delete the two last element of the list which are LastpageNbr and canSearch
                    del fdata[-1]
                    del fdata[-1]

                with open("{}.json".format(enterUrl), 'w') as outfile:
                    """for item in data:
                        if item not in fdata:
                           fdata.append(item)"""
                    fdata.append({"LastpageNbr": LastpageNbr})
                    fdata.append({"canSearch": canSearch})
                    json.dump(fdata, outfile)
            except FileNotFoundError:
                pass

        else:
            try:
                with open("{}.json".format(enterUrl), 'w') as outfile:
                    data.append({"LastpageNbr": LastpageNbr})
                    data.append({"canSearch": canSearch})
                    json.dump(data, outfile)

            except FileNotFoundError:
                pass


    def GetLastPageNumber(self, enterUrl):

        os.chdir(self.cacheFolderPath)
        try:

            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-2]['LastpageNbr']
        except FileNotFoundError:
            return None
        return lastNumber



    def verifyIfFileExist(self,enterUrl):
        os.chdir(self.cacheFolderPath)
        try:
            if os.path.isfile("{}.json".format(enterUrl)):
                return True
            else:
                return False
        except FileNotFoundError:
            pass

    def readFile(self, enterUrl):
        # open the folder and return its contents
        os.chdir(self.cacheFolderPath)
        try:
            with open("{}.json".format(enterUrl), "r") as printer:
                fileContent = json.load(printer)
                return fileContent
        except FileNotFoundError:
            pass



    def updateCanSearch(self,enterUrl):
        os.chdir(self.cacheFolderPath)
        fdata = []
        try:
            with open("{}.json".format(enterUrl), 'r') as outfile:
                fdata = json.load(outfile)
                del fdata[-1]
            with open("{}.json".format(enterUrl), 'w') as outfile:
                fdata.append({"canSearch": False})
                json.dump(fdata, outfile)
        except FileNotFoundError:
            pass


    """"
    For Lead Search: Using leadFolderPath
    """
    def verifyIfFileExist2(self, enterUrl):
        # All files that correspond to the search
        files = []
        os.chdir(self.leadFolderPath)
        for fileName in os.listdir(self.leadFolderPath):
            if enterUrl in fileName.lower():
                files.append(fileName)
        if len(files) > 0:
            return files
        else:
            return False


    def readFile2(self, files):
        # open the folder and return its contents
        os.chdir(self.leadFolderPath)
        if len(files) == 1:
            try:
                with open("{}".format(files[0]), "r") as printer:
                    fileContent = json.load(printer)
                    return fileContent
            except FileNotFoundError:
                pass
        else:
            fileContent = ''
            for file in files:
                try:
                    with open("{}".format(file), "r") as printer:
                        if file == files[0]:
                            fileContent = json.load(printer)
                        else:
                            otherFileContent = json.load(printer)
                            # Append other data on the Json file
                            fileContent[0]['Results'].extend(otherFileContent[0]['Results'])
                except FileNotFoundError:
                    pass
            return fileContent





