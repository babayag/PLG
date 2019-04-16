from .models import Forfait
from .models import Payment
from .models import SpaUser
from .models import Search
from .serializers import ForfaitSerializer
from .serializers import PaymentSerializer
from .serializers import UserSerializer
from .serializers import SearchSerializer
import datetime
from dateutil.parser import parse

class Transaction():
   
   # Read all forfait in forfait models
    def getforfait(self):
        forfait = Forfait.objects.all()
        serializer= ForfaitSerializer(forfait,many=True)
        return serializer.data

    # return list of all payements of the user who has user_id
    def getPayementinfo(self,user_id):
        payement = Payment.objects.get(user_id = user_id)
        serializer= PaymentSerializer(payement)
        return serializer.data

    # get save  payement of current user
    def SavePayment(self, userEmail, forfait_id):
        User = SpaUser.objects.get(email = userEmail)
        #return the forfait that match with forfait_id
        forfait = Forfait.objects.get(id = forfait_id)  

        
        User.niche_number = int(User.niche_number) + int(forfait.niche)
        User.save()
       
        payment = Payment()
        payment.user_id = User.id
        payment.forfait_id = forfait.id
        payment.isValid = True
        payment.currency = "USD"
        payment.save()
           
        return PaymentSerializer(payment).data

    # this method get all payement of current user
    def getAllPayment(self,userEmail):
        Historic = []
        User = SpaUser.objects.get(email = userEmail)
        # get all payement of current user order by created_at desc innerjoin forfait table
        payements = Payment.objects.filter(user_id = User.id).order_by('-created_at').select_related('forfait')
        for payement in payements:
            data = {
                    "description": payement.forfait.description,
                    "price" : payement.forfait.price,
                    "date" :  (payement.created_at).ctime(),
                    "Isvalid" : payement.isValid
                    }
            Historic.append(data)
        return Historic

    # get the rest of request of the current user
    def getRestOfRequestOfUser(self, userEmail):
        User = SpaUser.objects.get(email = userEmail)
        return User.niche_number
    

    def SaveUserSearch(self,newNiche,newLocation,userEmail):
        # laod the user whose email is userEmail
        User = SpaUser.objects.get(email = userEmail)
        # Get all the searches this user has ever made
        allCurrentUserSearches = Search.objects.filter(user_id = User.id)
        # Check if the new search exists already
        eventualNewSearch = Search.objects.filter(user_id = User.id, niche = newNiche, location = newLocation)

        # if the seach exists, we dont decrement the number of searches (nicheNumber)
        if eventualNewSearch :
           
            print("already exist")
        # if not, we decrement this number
        else : 

            User.niche_number = int(User.niche_number) - 1
            User.save()

            # create a new record in search table and set value to each field
            newSearch = Search()
            newSearch.niche = newNiche
            newSearch.location = newLocation
            newSearch.user_id = User.id
            newSearch.save()

        return SearchSerializer(eventualNewSearch, many=True).data

    def getAllSearchOfUser(self,userEmail):
        User = SpaUser.objects.get(email = userEmail)
        # get all search of current user order by created_at 
        searchList = Search.objects.filter(user_id = User.id).order_by('-created_at')
        
        return SearchSerializer(searchList, many=True).data
    


    