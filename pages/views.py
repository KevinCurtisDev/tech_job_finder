from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from jobs.models import Job

def index(request):
    #Render a htmltemplate view for the home page
    return render(request, 'pages/index.html')


def about(request):
    #Render a htmltemplate view for the about page
    return render(request, 'pages/about.html')