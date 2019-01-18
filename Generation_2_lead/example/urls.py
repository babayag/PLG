from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.LeadListCreate.as_view()),
    path('<int:pk>/', views.DetailLead.as_view()),
    path('share', views.ShareView.as_view()),
    path('testSharing', views.TestSharingView.as_view()),
]