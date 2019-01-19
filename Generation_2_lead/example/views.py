
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response

#from .emailsfinder import EmailFinderService
from .BingSearch import BingSearch
from .Email import Email
from .JsonStructure import JsonStructure

# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DetailLead(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class ShareView(APIView):
    permission_classes = []


class TestSharingView(APIView) :
    def post(self, request):
        enterUrl = request.data.get('url', None)

        #BingSearch.__init__(BingSearch, enterUrl)
        #a = BingSearch.search(BingSearch)
        Email.__init__(Email)
        b = Email.getEmail(Email, enterUrl)
        #JsonStructure.__init__(JsonStructure, b)
        #c = JsonStructure.JsonStructureReturn(JsonStructure)
        Jsonfinal = {"data": b}
        return Response(Jsonfinal)

