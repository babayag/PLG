
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# from knox.models import AuthToken
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response

# from .serializers import CreateUserSerializer, UserSerializer , LoginUserSerializer
from .SearchOnMultipleDomain import SearchOnMultipleDomain
from .Email import Email
from .GenerateValidEmail import GenerateValidEmail

# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DetailLead(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

# class RegistrationAPI(generics.GenericAPIView):
#     serializer_class = CreateUserSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)
#         })

# class LoginAPI(generics.GenericAPIView):
    
#     serializer_class = LoginUserSerializer

#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         serializer = self.get_serializer(data=request.data)
#         print(serializer)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         print(user)
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)
#         })

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
        Domains1 = request.data.get('domains1', None)
        Domains2 = request.data.get('domains2', None)
        Domains = [Domains1,Domains2]
       
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
