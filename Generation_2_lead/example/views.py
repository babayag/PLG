
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.utils.decorators import method_decorator


from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response
from .emailsfinder import EmailFinderService

from .emailsfinder import EmailFinderService

# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DetailLead(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class ShareView(APIView):
    permission_classes = []

    def post(self, request):
        enterUrl = request.data.get('url', None)
        EmailFinderService.getEmail(enterUrl)
        Alldata = EmailFinderService.getEmail(enterUrl)
        Jsonfinal = {"data": Alldata}
        return Response(Jsonfinal)

class TestSharingView(APIView) :
    def post(self, request):
        enterUrl = request.data.get('url', None)
        Alldata = EmailFinderService.getEmail(EmailFinderService, enterUrl)
        Jsonfinal = {"data": Alldata}
        return Response(Jsonfinal)

