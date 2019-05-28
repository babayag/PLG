from rest_framework.views import APIView
# from knox.models import AuthToken
from .models import Lead, Search, SpaUser
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


"""
author : Domngang Eric Faycal, Essongo joel Stephane
description : endpoints for getting email when we entry a domain 
"""
class TestSharingView(APIView): 
    def post(self, request):
        EnterUrl = request.data.get('url', None)
        p = request.data.get('p', None)
        FinalData = Email.main(Email, EnterUrl, p)# p = nomber of email to back
        Jsonfinal = {"data": FinalData}

        return Response(Jsonfinal)


"""
author : Essongo joel Stephane
description : endpoints for updating cache file for search on a domain 
"""    
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

"""
author : Domngang Eric Faycal, Essongo joel Stephane
description : endpoints for getting email to download it 
"""
class DownloadEmailInCsv(APIView):
    def post(self, request):
        EnterUrl = request.data.get('url', None)
        Email.__init__(Email)
        EmailsAnsSources = Email.DownloadEmails(Email, EnterUrl)
        Data = {'data': EmailsAnsSources}
        return Response(Data)

"""
author : Ranyl Foumbi
description : endpoints for getting email when we entry a multiple domain 
"""
class SearchMultipledomain(APIView):
    def post(self, request):
        Domains = request.data.get('domains', None)
        MoreDomain = SearchOnMultipleDomain.VerifyUrlAndSearchEmail(SearchOnMultipleDomain,Domains)
        DataMore = {'data': MoreDomain}
        return Response(DataMore)

"""
author : Domngang Eric Faycal
description : search valid email according to the domain , fistname , lastname 
"""        
class CreateEmailView(APIView): 
    def post(self, request):
        firstname = request.data.get('firstname', None)
        lastname = request.data.get('lastname', None)
        domain = request.data.get('domain', None)
          
        ValidEmails = GenerateValidEmail.ReturnValidEmail(GenerateValidEmail,firstname,lastname,domain)

        return Response(ValidEmails)

"""
author : Essongo Joel Stephane
description : endpoints for getting email when we enter niche and location
"""
class FindYourLeads(APIView):
    def post(self, request):
        EnteredNiche = request.data.get('niche', None)
        EnteredCity = request.data.get('city', None)
        EmailsAndSourceToParse = FindLeads.finder(FindLeads, EnteredNiche, EnteredCity)
        DatasToReturn = {'data': EmailsAndSourceToParse}
        return Response(DatasToReturn)

"""
author : Nouboussi Junior , Kevin Ngaleu
description : endpoints for getting email when we enter niche and location (user is not connected)
"""
class NormalFindLead(APIView): 
    def post(self, request):
        EnteredNiche = request.data.get('niche', None)
        EnteredCity = request.data.get('city', None)
        p = request.data.get('p', None) #this is the value we will use to search new emails
        
        FinalData = FindLeads.FindLead(FindLeads, EnteredNiche, EnteredCity , p)
        Jsonfinal = {"data": FinalData}

        return Response(Jsonfinal)
"""
author : Nouboussi Junior 
description : endpoints for getting email when we enter niche and location (user is connected)
"""
class BetterFindLead(APIView): 
    def post(self, request):
        EnteredNiche = request.data.get('niche', None)
        EnteredCity = request.data.get('city', None)
        UserEmail = request.data.get('email', None)
        p = request.data.get('p', None) #this is the value we will use to search new emails
       
        # if user request is finished (== 0)
        if Transaction.GetRestOfRequestOfUser(Transaction,UserEmail) == 0: 
            # if the curent search already exist in search table return result to the user
            try:
                User = SpaUser.objects.get(email = UserEmail)
                eventualNewSearch = Search.objects.get(user_id = User.id, niche = EnteredNiche, location = EnteredCity)
                FinalData = FindLeads.FindLead(FindLeads, EnteredNiche, EnteredCity , p)
                Jsonfinal = {"data": FinalData} 
                return Response(Jsonfinal)
            # if not, display this message
            except:
                return Response("Your are at the end of your subscription, please make a new subscription ! !")
        # if user request is not finished (not  null) always return result
        else:
            FinalData = FindLeads.FindLead(FindLeads, EnteredNiche, EnteredCity , p)
            Transaction.SaveUserSearch(Transaction,EnteredNiche,EnteredCity,UserEmail)
            Jsonfinal = {"data": FinalData}

            return Response(Jsonfinal)


"""
author : Nouboussi Junior , Essongo Joel Stephane 
description : endpoints for getting if a domain has a fb or google pixel
"""
class CheckPixels(APIView): 
    def post(self, request):
        domain = request.data.get('domain', None)
        FinalData = FindLeads.CheckPixel(FindLeads, domain)
        Jsonfinal = {"data": FinalData}
        return Response(Jsonfinal)
        
        

"""
author : Nouboussi Junior , Domngang Eric Faycal 
description : endpoints for create payment on paypal
"""

class PaypalCreatePayment(APIView):
    def post(self, request):
        ForfaitId = request.data.get('idForfait', None)
        payment = Paypal.createPayment(Paypal,ForfaitId)
        return Response(payment)

"""
author : Nouboussi Junior , Domngang Eric Faycal 
description : endpoints for verifying if the payment is valid before store it
"""

class PaypalExecutePayment(APIView): 
    def post(self, request):
        paymentId = request.data.get('paymentId', None)
        PayerID = request.data.get('PayerID', None)
        token = request.data.get('token', None)
        UserEmail = request.data.get('email', None)
        ForfaitId = request.data.get('idForfait', None)  
        FinalData = Paypal.executePayment(Paypal, PayerID, paymentId, token,UserEmail,ForfaitId)
        Jsonfinal = {"data": FinalData}

        return Response(Jsonfinal)

"""
author : Ranyl Foumbi
description : endpoints for getting email when we enter niche and location (user is not connected)
"""
class GetAllForfait(APIView):
    def post(self, request):
        AllForfait = Transaction.getforfait(Transaction)
        return Response(AllForfait)
"""
author : Ranyl Foumbi
description : endpoints for getting all user payment
"""
class GetAllPayment(APIView):
    def post(self, request):
        UserEmail = request.data.get('email', None)
    
        AllPayment = Transaction.GetAllPayment(Transaction,UserEmail)
        return Response(AllPayment)
"""
author : Ranyl Foumbi
description : endpoints for getting rest of a user request
"""
class GetRestUserRequest(APIView):
    def post(self, request):
        UserEmail = request.data.get('email', None)
        rest = Transaction.GetRestOfRequestOfUser(Transaction,UserEmail)
        return Response(rest)


"""
author : Ranyl Foumbi
description : endpoints for getting all user search
"""
class GetAllUserSearch(APIView):
     def post(self, request):
        UserEmail = request.data.get('email', None)
        result = Transaction.GetAllSearchOfUser(Transaction,UserEmail)
        return Response(result)
         