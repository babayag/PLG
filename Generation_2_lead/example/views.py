
from rest_framework.response import Response
from rest_framework.views import APIView
from .Email import EmailFinderService
from .BingSearch import BingSearch

from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics


# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DetailLead(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class MyOwnView(APIView):
    def post(self, request):
        enterUrl = request.data.get('url', None)
       # Alldata = EmailFinderService.getEmail(EmailFinderService,enterUrl)
        BingSearch.__init__(self,enterUrl)
        driver = BingSearch.search(self)
        EmailFinderService.__init__(self, driver)
        c = EmailFinderService.getEmail(self,enterUrl)
        print(c)
     #   Jsonfinal = {"data": Alldata}
        return c

