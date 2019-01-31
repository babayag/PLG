
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .BingSearch import BingSearch

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
        if BingSearch.UrlValidation(BingSearch,enterUrl) == True:
            Email.__init__(Email)
            finalData = Email.getEmail(Email, enterUrl)
            Jsonfinal = {"data": finalData}
            return Response(Jsonfinal)
        else:
            return Response("YOU ENTERED A BAD URL !")

    
class UpdateJsonFile(APIView):
    def post(self, request):
        response = False
        enterUrl = request.data.get('url', None)
        if BingSearch.UrlValidation(BingSearch, enterUrl) == True:
            Email.__init__(Email)
            finalData = Email.getEmail(Email, enterUrl)
            Jsonfinal = {"data": finalData}
            if len(Jsonfinal) != 0:
                response = True
            else:
                response = False
            return Response(response)
        else:
            return Response("YOU ENTERED A BAD URL !")

