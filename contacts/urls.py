from django.urls import path

from . import views

#set up urls for contacts app
urlpatterns = [
    path('contact', views.contact, name='contact')
]
    
