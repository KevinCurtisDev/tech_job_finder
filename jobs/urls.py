from django.urls import path

from . import views

#set up urls for the jobs app
urlpatterns = [
    path('', views.index, name='jobs'),
    path('<int:job_id>', views.job, name='job'),
    path('search', views.search, name='search'),
]