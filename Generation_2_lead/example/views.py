from rest_framework.views import APIView
# from knox.models import AuthToken
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response

from .Transaction import Transaction
# from .serializers import CreateUserSerializer, UserSerializer , LoginUserSerializer
from .SearchOnMultipleDomain import SearchOnMultipleDomain
from .Email import Email
from .GenerateValidEmail import GenerateValidEmail
from .FinLeads import FindLeads
from .Paypal import Paypal

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


class BetterFindLead(APIView): 
    def post(self, request):
        enteredNiche = request.data.get('niche', None)
        enteredCity = request.data.get('city', None)
        finalData = FindLeads.findLead(FindLeads, enteredNiche, enteredCity)
        Jsonfinal = {"data": finalData}

        return Response(Jsonfinal)


class PaypalCreatePayment(APIView):
    def post(self, request):
        forfait_id = request.data.get('idForfait', None)
        payment = Paypal.createPayment(Paypal,forfait_id)
        return Response(payment)


class PaypalExecutePayment(APIView): 
    def post(self, request):
        paymentId = request.data.get('paymentId', None)
        PayerID = request.data.get('PayerID', None)
        token = request.data.get('token', None)
        user_email = request.data.get('email', None)
        forfait_id = request.data.get('idForfait', None)  
        print(user_email,forfait_id)
        finalData = Paypal.executePayment(Paypal, PayerID, paymentId, token,user_email,forfait_id)
        Jsonfinal = {"data": finalData}

        return Response(Jsonfinal)

class GetAllForfait(APIView):
    def post(self, request):
        allForfait = Transaction.getforfait(Transaction)
        return Response(allForfait)

class GetAllPayment(APIView):
    def post(self, request):
        user_email = request.data.get('user_email', None)
        allPayment = Transaction.getAllPayment(Transaction,user_email)
        return Response(allPayment)

class GetRestUserRequest(APIView):
    def post(self, request):
        user_email = request.data.get('user_email', None)
        rest = Transaction.getRestOfRequestOfUser(Transaction,user_email)
        return Response({"Rest of request":rest})

"""class SaveTransaction(APIView):
    def post(self, request): 
        user_email = request.data.get('user_email', None)
        forfait_id = request.data.get('forfait_id', None)
        tes = Transaction.SavePayment(Transaction,user_email,forfait_id)
        return Response(tes)"""