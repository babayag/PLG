from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
#path('', views.LeadListCreate.as_view()),
#path('<int:pk>/', views.DetailLead.as_view()),
url(r'^my-own-view/$', views.MyOwnView.as_view())
#path('email/', views.EmailsFinder)
]