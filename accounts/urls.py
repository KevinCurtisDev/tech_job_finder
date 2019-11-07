from django.urls import path

from . import views

#set upurl patterns for the accounts app
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]