from django.urls import path

from . import views

urlpatterns = [
    path('donation', views.donation, name='donation'),
    path('charge', views.charge, name='charge'),
]