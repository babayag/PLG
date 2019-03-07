from django.conf.urls import url
from django.urls import path , include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.LeadListCreate.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('<int:pk>/', views.DetailLead.as_view()),
    path('share', views.ShareView.as_view()),
    path('getAllDomains', views.SearchMultipledomain.as_view()),
    path('testSharing', views.TestSharingView.as_view()),
    path('updateJsonFile', views.UpdateJsonFile.as_view()),
    path('downloadEmails', views.DownloadEmailInCsv.as_view()),
    path('findervalidEmail', views.CreateEmailView.as_view()),
    path('nicheAndCity', views.GetEmailsByNicheAndCity.as_view()),

]


