import os
import json
from datetime import datetime
import time

class FileManager():
    """
    author : Essongo Joel Stepahne
    params : 
    description : initialize path for managing files on different location 
    """
    def __init__(self):
        self.CacheFolderPath = r'F:\SEMESTER 3\Software Product Design and Ergonomics\App\Project\Profitable LG\PLG\Generation_2_lead\example\cache'
        self.LeadFolderPath = r'F:\SEMESTER 3\Software Product Design and Ergonomics\App\Project\Profitable LG\PLG\Generation_2_lead\example\leads'

    """
    author : Essongo Joel Stepahne
    params : data, enterUrl, LastpageNbr, canSearch
    description : write in a json file (email found, url entered ,the LastpageNbr, and the boolean canSearch)
    return an object which contain (data, enterUrl, LastpageNbr, canSearch )  
    """
    def WriteInFile(self, data, enterUrl, LastpageNbr, canSearch):
        os.chdir(self.CacheFolderPath)
        if self.VerifyIfFileExist(self, enterUrl):
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
            return True

        else:
            try:
                with open("{}.json".format(enterUrl), 'w') as outfile:
                    data.append({"LastpageNbr": LastpageNbr})
                    data.append({"canSearch": canSearch})
                    json.dump(data, outfile)

            except FileNotFoundError:
                pass
            return False

    """
    author : Essongo Joel Stephane
    params : enterUrl 
    description : get the last page when we search email on an Enterurl to continue where we stop 
    return : a number lastNumberPage
    """
    def GetLastPageNumber(self, enterUrl):

        os.chdir(self.CacheFolderPath)
        try:

            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-2]['LastpageNbr']
        except FileNotFoundError:
            return None
        return lastNumber


    """
    author : Essongo Joel Stephane
    params : enterUrl
    description : verify if the file exist for a domain search 
    return a boolean which tell if file exist or no
    """
    def VerifyIfFileExist(self,enterUrl):
        os.chdir(self.CacheFolderPath)
        try:
            if os.path.isfile("{}.json".format(enterUrl)):
                return True
            else:
                return False
        except FileNotFoundError:
            pass
    
    """
    author : Essongo Joel Stephane
    params : enterUrl
    description : ReadFile for a domain search 
    return an object FileContent
    """
    def ReadFile(self, enterUrl):
        # open the folder and return its contents
        os.chdir(self.CacheFolderPath)
        try:
            with open("{}.json".format(enterUrl), "r") as printer:
                FileContent = json.load(printer)
                return FileContent
        except FileNotFoundError:
            pass


    """
    author : Essongo Joel Stephane
    params : enterUrl
    description : update the value canSearch to true or false.
    return: return a boolean wich tell if we can search email again or no
    """
    def UpdateCanSearch(self,enterUrl):
        os.chdir(self.CacheFolderPath)
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


    """
    author : Kevin Ngaleu
    params : enterUrl
    description : verify if the file exist for a domain search. in this case we use it for lead folder 
    return: a boolean wich tell if file exist or no
    """
    def VerifyIfFileExist2(self, enterUrl):
        # All Files that correspond to the search
        Files = []
        os.chdir(self.LeadFolderPath)
        for fileName in os.listdir(self.LeadFolderPath):
            if enterUrl in fileName.lower():
                Files.append(fileName)
        if len(Files) > 0:
            return Files
        else:
            return False

    """
    author : kevin Ngaleu
    params : Files
    description : read files in the lead folder 
    return an object FileContent
    """
    def ReadFile2(self, Files):
        # open the folder and return its contents
        os.chdir(self.LeadFolderPath)
        if len(Files) == 1:
            try:
                with open("{}".format(Files[0]), "r") as printer:
                    FileContent = json.load(printer)
                    return FileContent
            except FileNotFoundError:
                pass
        else:
            FileContent = ''
            for file in Files:
                try:
                    with open("{}".format(file), "r") as printer:
                        if file == Files[0]:
                            FileContent = json.load(printer)
                        else:
                            OtherFileContent = json.load(printer)
                            # Append other data on the Json file
                            FileContent[0]['Results'].extend(OtherFileContent[0]['Results'])
                except FileNotFoundError:
                    pass
            return FileContent





