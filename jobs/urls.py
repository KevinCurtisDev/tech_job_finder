from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='jobs'),
    path('<int:job_id>', views.job, name='job'),
    path('search', views.search, name='search'),
]