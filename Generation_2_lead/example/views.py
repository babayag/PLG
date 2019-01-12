import self as self
from knox.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import views, request

import simplejson as json
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics, views

from .emailsfinder import EmailFinderService

import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DetailLead(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


#class MyOwnView(APIView):
   # def post(self, request):
        #a: int = request.data
        #b: int = 5
        #s: int = a + a
    #   return Response(request.data)

class MyOwnView(APIView):
    def post(self, request):
        enterUrl = request.data.get('url',None)
        EmailFinderService.getEmail(enterUrl)
        Alldata = EmailFinderService.getEmail(enterUrl)
        Jsonfinal = {"data": Alldata}
        return Response(Jsonfinal)

