
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response

from .SearchOnMultipleDomain import SearchOnMultipleDomain
from .Email import Email

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
        enterUrl1 = request.data.get('url1', None)
        enterUrl2 = request.data.get('url2', None)
        enterUrl3 = request.data.get('url3', None)
        enterUrl4 = request.data.get('url4', None)
        enterUrl5 = request.data.get('url5', None)
        enterUrl6 = request.data.get('url6', None)
        enterUrl7 = request.data.get('url7', None)
        Domains = [enterUrl1,enterUrl2,enterUrl3,enterUrl4, enterUrl5,enterUrl6,enterUrl7 ]

        moreDomain = SearchOnMultipleDomain.verifyUrlAndSearchEmail(SearchOnMultipleDomain,Domains)
        Datamore = {'data': moreDomain}
        return Response(Datamore)
