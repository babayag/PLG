from django.conf.urls import url
from django.urls import path , include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.LeadListCreate.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # url(r'^social/login', include('rest_social_auth.urls_token')),
    # path('auth/', include('knox.urls')),
    # path('auth/register/', views.RegistrationAPI.as_view()),
    # path('auth/login/', views.LoginAPI.as_view()),
    #path('<int:pk>/', views.DetailLead.as_view()),
    path('share', views.ShareView.as_view()),
    path('bulksearch', views.SearchMultipledomain.as_view()),
    path('testSharing', views.TestSharingView.as_view()),
    path('updateJsonFile', views.UpdateJsonFile.as_view()),
    path('downloadEmails', views.DownloadEmailInCsv.as_view()),
    path('findervalidEmail', views.CreateEmailView.as_view()),
    path('findLeads', views.FindYourLeads.as_view()),
    #find leads from dashboard
    path('betterfindlead', views.BetterFindLead.as_view()),
    #find leads when not connected
    path('normalFindLeads', views.NormalFindLead.as_view()), 
    path('checkpixel', views.CheckPixels.as_view()),
    path('createPayment', views.PaypalCreatePayment.as_view()),
    path('getAllPayement', views.GetAllPayment.as_view()),
    path('executePayment', views.PaypalExecutePayment.as_view()),
    path('getAllforfait', views.GetAllForfait.as_view()),
    path('getRestOfrequest', views.GetRestUserRequest.as_view()),
    path('getallusersearch', views.GetAllUserSearch.as_view()),
]
