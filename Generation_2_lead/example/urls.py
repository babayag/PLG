from django.urls import path

from . import views

urlpatterns = [
    path('', views.LeadListCreate.as_view()),
    path('<int:pk>/', views.DetailLead.as_view()),
]