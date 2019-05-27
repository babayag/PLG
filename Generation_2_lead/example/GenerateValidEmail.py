#import needed object
import requests
import objectpath
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import datetime
import re
#import itertools
import sys

class GenerateValidEmail():
    """
    author : Domngang Eric Faycal and bryan Mingana
    params : name , PatternFirstnameAndLastname  
    description : cut the process if the name is not matchinf a pattern
    """
    def printInvalidEntry(self,name,PatternFirstnameAndLastname):
        #print a message and stop the program if the name is not matching the pattern or is empty
        if PatternFirstnameAndLastname.search(name)or name == "":
            pass
        else:
            #sys.exit("Invalid {0}".format([ k for k,v in locals().iteritems() if v == name][0]))
            print("Sorry, but the firstname or the lastname is invalid")
            sys.exit()
        return 0
    
    """
    author : Domngang Eric Faycal and bryan Mingana
    params : name , firstname , lastname, DomainName  
    description : verify the defferent params according to the pattern
    """
    def VerifyEntry(self,firstname,lastname,DomainName):
    #method which verify is what the user enter match with the firstname, lastname or domain parttern
        #set firstname and lastname pattern : return the object PatternFirstnameAndLastname of type _sre.SRE_Pattern
        PatternFirstnameAndLastname = re.compile("^[\w\_\-\.\ ]+$")
        # set domain pattern : return the object PatternDomain of type _sre.SRE_Pattern
        PatternDomain = re.compile("^\w+\.\w+$")
        #verify if firstname is valid        
        self.printInvalidEntry(self,firstname,PatternFirstnameAndLastname)
        #verify if lastname is valid 
        self.printInvalidEntry(self,lastname,PatternFirstnameAndLastname)

        #print a message and stop the program if the domain is not matching the pattern or is empty
        if PatternDomain.search(DomainName):
            pass
        else:
            print("Sorry , but you enter an invalid Domain")
            sys.exit()
        return 0
    
    """
    author : Domngang Eric Faycal and bryan Mingana
    params : firstname,lastname,DomainName,ListOfEmails
    description : generate possible random email 
    """   
    def GeneratePossibleMailWithTwoEntry(self,firstname,lastname,DomainName,ListOfEmails):
    #generate all the possible email with two name and keep them in ListOfEmails : return an object of type int
        email1 =  firstname[0]+lastname+"@"+DomainName
        ListOfEmails.append(email1)
        email2 =  firstname+"."+lastname+"@"+DomainName
        ListOfEmails.append(email2)
        email3 =  lastname+"@"+DomainName
        ListOfEmails.append(email3)
        email4 =  firstname+"_"+lastname+"@"+DomainName
        ListOfEmails.append(email4)
        email5 =  firstname[0]+"_"+lastname+"@"+DomainName
        ListOfEmails.append(email5)
        email6 =  firstname+lastname[0]+"@"+DomainName
        ListOfEmails.append(email6)
        email7 = firstname+"@"+DomainName
        ListOfEmails.append(email7)
        email8 = firstname[0]+"@"+DomainName
        ListOfEmails.append(email8)
        email9 = lastname[0]+"@"+DomainName
        ListOfEmails.append(email9)
        email10 = firstname[0]+lastname[0]+"@"+DomainName
        ListOfEmails.append(email10)
        email11 = firstname+lastname+"@"+DomainName
        ListOfEmails.append(email11)
        email12 = lastname+firstname+"@"+DomainName
        ListOfEmails.append(email12)
        email13 =  lastname+"."+firstname+"@"+DomainName
        ListOfEmails.append(email13)
        email14 =  lastname[0]+firstname+"@"+DomainName
        ListOfEmails.append(email14)
        
    """
    author : Domngang Eric Faycal and bryan Mingana
    params : name,DomainName, ListOfEmails
    description : generate possible random email 
    """  
    def GeneratePossibleMailWithOneEntry(self,name,DomainName, ListOfEmails):
            
        email1 =  name[0]+"@"+DomainName
        ListOfEmails.append(email1)
        email2 =  name+"@"+DomainName
        ListOfEmails.append(email2)
        email3 =  "_"+name+"@"+DomainName
        ListOfEmails.append(email3)

    """
    author : Domngang Eric Faycal and bryan Mingana
    params : firstname,lastname,DomainName
    description : generate possible random email 
    """
    
    def GeneratePossibleMail(self,firstname,lastname,DomainName):
        """
        Get first, last name and domain name, and return a list of possible mail
        """
        #initialise the object that will contain all possible name, return the object listOfEmai
        ListOfEmails = []
        if len(firstname)> 0 and len(lastname)> 0:
            self.GeneratePossibleMailWithTwoEntry(self,firstname,lastname,DomainName,ListOfEmails)
        elif firstname=="" and len(lastname)> 0:
            self.GeneratePossibleMailWithOneEntry(self,lastname,DomainName, ListOfEmails)
        elif len(firstname)> 0 and lastname == "":
            self.GeneratePossibleMailWithOneEntry(self,firstname,DomainName, ListOfEmails)
        else:
            print("Sorry, but you didn't enter neither a firstname or a lastname")
            sys.exit()
        return ListOfEmails

    """
    author : Domngang Eric Faycal and bryan Mingana
    params : firstname,lastname,DomainName,ListOfEmails
    description : verify if email exist
    """  
    def VerifyEmail(self,email):
        key = '5c78147010c89'
        RequestUrl = "https://api.debounce.io/v1/?api={0}&email={1}&append=false".format(key,email)
        request = requests.post(RequestUrl)
        request = request.json()
        jsonTree = objectpath.Tree(request['debounce'])
        resultTuple = tuple(jsonTree.execute('$..result'))
        result = False
        for report in resultTuple:
            if report == 'Safe to Send':
                result = email
            elif report == 'Risky':
                result = email
            else:
                pass
            
        return result

    """
    author : Domngang Eric Faycal and bryan Mingana
    params : firstname,lastname,DomainName,ListOfEmails
    description : Return valid email  
    """  
    def ReturnValidEmail(self,firstname,lastname,DomainName):

        self.VerifyEntry(self,firstname,lastname,DomainName)
        ValidEmails = []
        debut = datetime.datetime.now()
        ListOfEmails = self.GeneratePossibleMail(self,firstname,lastname,DomainName)
        with PoolExecutor(max_workers=7) as executor:
                for email in ListOfEmails:
                    emails = self.VerifyEmail(self,email)
                    if emails == False:
                        pass
                    else:
                        ValidEmails.append(email)
                    
        if len(ValidEmails)> 0 :
            print("Final result : Valid mail")
            for mail in ValidEmails:
                print(mail)
        else:
            print("Sorry, there's no valid emails for those informations")
        return ValidEmails
