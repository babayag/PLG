
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics

from .emailsfinder import EmailFinderService

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
        Alldata = EmailFinderService.getEmail(EmailFinderService,enterUrl)
        Jsonfinal = {"data": Alldata}
        return Response(Jsonfinal)

