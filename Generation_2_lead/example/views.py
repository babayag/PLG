from rest_framework.views import APIView

from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response

from .SearchOnMultipleDomain import SearchOnMultipleDomain
from .Email import Email
from .GenerateValidEmail import GenerateValidEmail
from .FinLeads import FindLeads

# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DetailLead(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class ShareView(APIView):
    permission_classes = []


class TestSharingView(APIView): 
    def post(self, request):
        enterUrl = request.data.get('url', None)
        p = request.data.get('p', None)
        finalData = Email.main(Email, enterUrl, p)# p = nomber of email to back
        Jsonfinal = {"data": finalData}

        return Response(Jsonfinal)


    
class UpdateJsonFile(APIView):
    def post(self, request):
        response = False
        enterUrl = request.data.get('url', None)
        finalData = Email.main(Email, enterUrl)
        print(finalData)
        Jsonfinal = {"data": finalData}
        if len(Jsonfinal) != 0:
            response = True
        else:
            response = False
        return Response(response)

class DownloadEmailInCsv(APIView):
    def post(self, request):
        enterUrl = request.data.get('url', None)
        Email.__init__(Email)
        emailsAnsSources = Email.DownloadEmails(Email, enterUrl)
        Data = {'data': emailsAnsSources}
        return Response(Data)

class SearchMultipledomain(APIView):
    def post(self, request):
        Domains = request.data.get('domains', None)
        moreDomain = SearchOnMultipleDomain.verifyUrlAndSearchEmail(SearchOnMultipleDomain,Domains)
        Datamore = {'data': moreDomain}
        return Response(Datamore)
        
class CreateEmailView(APIView): 
    def post(self, request):
        firstname = request.data.get('firstname', None)
        lastname = request.data.get('lastname', None)
        domain = request.data.get('domain', None)
          
        validEmails = GenerateValidEmail.returnValidEmail(GenerateValidEmail,firstname,lastname,domain)

        return Response(validEmails)

class FindYourLeads(APIView):
    def post(self, request):
        enteredNiche = request.data.get('niche', None)
        enteredCity = request.data.get('city', None)
        emailsAndSourceToParse = FindLeads.finder(FindLeads, enteredNiche, enteredCity)
        datasToReturn = {'data': emailsAndSourceToParse}
        return Response(datasToReturn)
