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
        self.CacheFolderPath = r'/media/byebyeman/_home/project/LeadMeHome/Generation_2_lead/example/cache/'
        self.LeadFolderPath = r'/media/byebyeman/_home/project/LeadMeHome/Generation_2_lead/example/leads/'
    """
    author : Essongo Joel Stephane
    params : Data , EnterUrl , LastpageNbr , CanSearch
    description : write in the file the params lastpageNnbr and can search for an url using on a search 
    """
    def WriteInFile(self, Data, EnterUrl, LastpageNbr, CanSearch):
        os.chdir(self.CacheFolderPath)
        if self.VerifyIfFileExist(self, EnterUrl):
            fdata = []
            try:
                with open("{}.json".format(EnterUrl), 'r') as outfile:
                    fdata = json.load(outfile)
                    # delete the two last element of the list which are LastpageNbr and CanSearch
                    del fdata[-1]
                    del fdata[-1]

                with open("{}.json".format(EnterUrl), 'w') as outfile:
                    """for item in Data:
                        if item not in fdata:
                           fdata.append(item)"""
                    fdata.append({"LastpageNbr": LastpageNbr})
                    fdata.append({"CanSearch": CanSearch})
                    json.dump(fdata, outfile)
            except FileNotFoundError:
                pass

        else:
            try:
                with open("{}.json".format(EnterUrl), 'w') as outfile:
                    Data.append({"LastpageNbr": LastpageNbr})
                    Data.append({"CanSearch": CanSearch})
                    json.dump(Data, outfile)

            except FileNotFoundError:
                pass

    """
    author : Essongo Joel Stephane
    params : EnterUrl 
    description : get the last page when we search email on an Enterurl to continue where we stop 
    """
    def GetLastPageNumber(self, EnterUrl):

        os.chdir(self.CacheFolderPath)
        try:

            with open("{}.json".format(EnterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-2]['LastpageNbr']
        except FileNotFoundError:
            return None
        return lastNumber


    """
    author : Essongo Joel Stephane
    params : EnterUrl
    description : verify if the file exist for a domain search 
    """
    def VerifyIfFileExist(self,EnterUrl):
        os.chdir(self.CacheFolderPath)
        try:
            if os.path.isfile("{}.json".format(EnterUrl)):
                return True
            else:
                return False
        except FileNotFoundError:
            pass
    
    """
    author : Essongo Joel Stephane
    params : EnterUrl
    description : ReadFile for a domain search 
    """
    def ReadFile(self, EnterUrl):
        # open the folder and return its contents
        os.chdir(self.CacheFolderPath)
        try:
            with open("{}.json".format(EnterUrl), "r") as printer:
                FileContent = json.load(printer)
                return FileContent
        except FileNotFoundError:
            pass


    """
    author : Essongo Joel Stephane
    params : EnterUrl
    description : update the value canSearch to true or false.
    """
    def UpdateCanSearch(self,EnterUrl):
        os.chdir(self.CacheFolderPath)
        fdata = []
        try:
            with open("{}.json".format(EnterUrl), 'r') as outfile:
                fdata = json.load(outfile)
                del fdata[-1]
            with open("{}.json".format(EnterUrl), 'w') as outfile:
                fdata.append({"CanSearch": False})
                json.dump(fdata, outfile)
        except FileNotFoundError:
            pass


    """
    author : Kevin Ngaleu
    params : EnterUrl
    description : verify if the file exist for a domain search. in this case we use it for lead folder 
    """
    def VerifyIfFileExist2(self, EnterUrl):
        # All Files that correspond to the search
        Files = []
        os.chdir(self.LeadFolderPath)
        for fileName in os.listdir(self.LeadFolderPath):
            if EnterUrl in fileName.lower():
                Files.append(fileName)
        if len(Files) > 0:
            return Files
        else:
            return False

    """
    author : kevin Ngaleu
    params : Files
    description : read files in the lead folder 
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
                            # Append other Data on the Json file
                            FileContent[0]['Results'].extend(OtherFileContent[0]['Results'])
                except FileNotFoundError:
                    pass
            return FileContent





