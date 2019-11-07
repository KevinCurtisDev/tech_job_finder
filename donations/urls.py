from django.urls import path

from . import views

#set up urls for the donations app
urlpatterns = [
    path('donation', views.donation, name='donation'),
    path('charge', views.charge, name='charge'),
]