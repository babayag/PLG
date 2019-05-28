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
   
    """
    author : Ranyl Foumbi
    params : 
    description:get the all forfait
    return: the list of all forfait in the db 
    """
    def GetForfait(self):
        forfait = Forfait.objects.all()
        serializer= ForfaitSerializer(forfait,many=True)
        return serializer.data

    """
    author : Ranyl Foumbi
    params : userEmail and forfait_id he choose
    description :   save the payment 
    return: the payment which is create
    """
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

    """
    author: Ranyl Foumbi
    params : userEmail
    description : get all payments
    return: the list of payment according to the userEmail
    """
    def GetAllPayment(self,userEmail):
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

    """
    author : Ranyl Foumbi
    params : userEmail
    description: get the list of the Rest Of the user Request
    return: the number of Rest Of the user request that a user can make to search niche and location

    """
    def GetRestOfRequestOfUser(self, userEmail):
        User = SpaUser.objects.get(email = userEmail)
        return User.niche_number
    
    """
    author : Ranyl Foumbi
    params : userEmail, newLocation , newNiche
    description: save search made by user 
    return:list of the search made by user
    """
    def SaveUserSearch(self,newNiche,newLocation,userEmail):
        # load the user whose email is userEmail
        User = SpaUser.objects.get(email = userEmail)

        # Check if the new search exists already
        try:
                EventualNewSearch = Search.objects.get(user_id = User.id, niche = newNiche, location = newLocation)
                EventualNewSearch.counter = (EventualNewSearch.counter) + 1
                EventualNewSearch.created_at = datetime.datetime.now()
                EventualNewSearch.save()
        # if not decrement niche number of user and create new search record
        except:
                User.niche_number = int(User.niche_number) - 1
                User.save()

                # create a new record in search table and set value to each field
                NewSearch = Search()
                NewSearch.niche = newNiche
                NewSearch.location = newLocation
                NewSearch.counter = 1
                NewSearch.user_id = User.id
                NewSearch.save()

    """
    author : Ranyl Foumbi
    params : userEmail
    description : get all searches of user
    return: the list of search according to the user email
    """
    def GetAllSearchOfUser(self,userEmail):
        User = SpaUser.objects.get(email = userEmail)
        # get all search of current user order by created_at 
        searchList = Search.objects.filter(user_id = User.id).order_by('-created_at')
        
        return SearchSerializer(searchList, many=True).data
    


    