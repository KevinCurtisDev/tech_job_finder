from django.urls import path

from . import views

#set upurls for the index and about pages
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]