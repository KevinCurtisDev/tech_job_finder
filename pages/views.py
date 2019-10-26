from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from jobs.models import Job

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')