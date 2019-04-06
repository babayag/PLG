from .models import Forfait
from .serializers import ForfaitSerializer
from .models import Payment
from .serializers import PaymentSerializer

class Transaction():
   
   # Read all forfait in forfait models
    def getforfait(self,request):
        forfait = Forfait.objects.all()
        serializer= ForfaitSerializer(forfait,many=True)

        return serializer.data

       
    