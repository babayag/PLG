
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response

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
        Jsonfinal = {"data": finalData}
        if len(Jsonfinal) != 0:
            response = True
        else:
            response = False
        return Response(response)

class DownloadEmailInCsv(APIView):
    def Get(self, request):
        enterUrl = request.data.get('url', None)
        Email.__init__(Email)
        emailsAnsSources = Email.DownloadEmails(Email, enterUrl)
        Data = {'data': emailsAnsSources}
        return Data
