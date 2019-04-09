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
        User = SpaUser.objects.get(email = userEmail)
        payement = Payment.objects.filter(user_id = User.id).order_by('created_at')
        serializer= PaymentSerializer(payement,many=True)
        return serializer.data

    def getRestOfRequestOfUser(self, userEmail):
        User = SpaUser.objects.get(email = userEmail)
        return User.niche_number
    
           