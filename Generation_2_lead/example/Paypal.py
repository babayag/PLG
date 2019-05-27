import paypalrestsdk
from paypalrestsdk import Payment
from .models import Payment
from .Transaction import Transaction
from .models import Forfait

class Paypal():
  """
    author : Domngang Eric Faycal and junior Nouboussi
    params : 
    description : configure the api key of paypal account
  """
  def configure(self):
    paypalrestsdk.configure({
      'mode': 'sandbox', #sandbox or live
      'client_id': 'AZBNmJ7wvdWNJxt4GN9YXT2IVV5ruG-0QGGqpvTS0YilnFbox9f5FPreXgyov2d6ozib-xAOk6ol5xbY',
      'client_secret': 'ELzSGWK_sr81DG0hV4mvXVuENWhe8iSBwajtx383IlzrlHMphUT63LbLWXnP3LFkQ-kxV5uIZU7Z0kZK' })

  """
    author : Domngang Eric Faycal and Junior Nouboussi
    params : forfait_id
    description : create the url for the payments process 
    return: an error or payment url 

  """
  def createPayment(self,forfait_id):

    forfait = Forfait.objects.get(id = forfait_id) 
    
    self.configure(self)

    # Create payment object
    payment = paypalrestsdk.Payment({
      "intent": "sale",

      # Set payment method
      "payer": {
        "payment_method": "paypal"
      },

      # Set redirect URLs
      "redirect_urls": {
        "return_url": "http://127.0.0.1:8000/dashboard/payment",
        "cancel_url": "http://127.0.0.1:8000/dashboard/payment"
      },

      # Set transaction object
      "transactions": [{
        "amount": {
          "total": forfait.price,
          "currency": "USD"
        },
        "description": forfait.description
      }]
    })
    print(payment)
    # Create payment
    if payment.create():
      # Extract redirect url
      for link in payment.links:
        if link.method == "REDIRECT":
          # Capture redirect url
          redirectUrl = (link.href)
          return {"redirect_url" : redirectUrl}
          # Redirect the customer to redirect_url

    else:
      print("Error while creating payment:")
      print(payment.error)
      return {"error": payment.error}

  """
    author : Domngang Eric Faycal and junior Nouboussi and Ranyl Foumbi
    params : paymentId, PayerId, token, user_email, forfait_id
    description : verify if the payement is valid before store it in our database
    return:object payment which contain the response status
  """
  def executePayment(self, PayerID, paymentId, token,user_email, forfait_id):

    self.configure(self)
   

    # Payment ID obtained when creating the payment (following redirect)
    payment = paypalrestsdk.Payment.find(paymentId)

    # Execute payment with the payer ID from the create payment call (following redirect)
    if payment.execute({"payer_id": PayerID}):
      print("Payment[%s] executed successfully" % (payment.id))

      Transaction.SavePayment(Transaction, user_email, forfait_id)
      
      return {"ok" : 1, "id" : payment.id}
    else:
      print(payment.error)
      return {"error": payment.error}
    