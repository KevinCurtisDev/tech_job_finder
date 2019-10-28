from django.urls import path

from . import views

urlpatterns = [
    path('donation', views.donation, name='donation'),
]