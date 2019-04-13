from .models import Forfait
from .models import Payment
from .models import SpaUser
from .serializers import ForfaitSerializer
from .serializers import PaymentSerializer
from .serializers import UserSerializer

class Transaction():
   
   # Read all forfait in forfait models
    def getforfait(self):
        forfait = Forfait.objects.all()
        serializer= ForfaitSerializer(forfait,many=True)
        return serializer.data

    
    def getPayementinfo(self,user_id):
        payement = Payment.objects.get(user_id = user_id)
        serializer= PaymentSerializer(payement)
        return serializer.data


    def SavePayment(self, userEmail, forfait_id):
        User = SpaUser.objects.get(email = userEmail)
        forfait = Forfait.objects.get(id = forfait_id)  

        
        User.niche_number = int(User.niche_number) + int(forfait.niche)
        User.save()
       
        payment = Payment()
        payment.user_id = User.id
        payment.forfait_id = forfait.id
        payment.currency = "USD"
        payment.save()
           
        return PaymentSerializer(payment).data


    def getAllPayment(self,userEmail):
        Historic =[]
        description = []
        prices = []
        date = []
        isvalid =  []
        User = SpaUser.objects.get(email = userEmail)
        payements = Payment.objects.filter(user_id = User.id).order_by('-created_at')
        for payement in payements:
            forfait = Forfait.objects.get(id = payement.forfait_id) 
            description.append(forfait.description)
            prices.append(forfait.price) 
            date.append(payement.created_at)
            isvalid.append(payement.isValid) 
        serializer= PaymentSerializer(payements,many=True)
        for i,j,k,m in zip(range(len(description)),range(len(prices)),range(len(date)),range(len(isvalid))):
            data = {
                    "description": description[i],
                    "price" : prices[j],
                    "date" : date[k],
                    "Isvalid" : isvalid[m]
                    }
            Historic.append(data)
        return Historic

    def getRestOfRequestOfUser(self, userEmail):
        User = SpaUser.objects.get(email = userEmail)
        return User.niche_number
    
           