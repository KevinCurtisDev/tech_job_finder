from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from jobs.models import Job

def index(request):
    jobs = Job.objects.order_by('-listed_date')[:3]

    context = {
        'jobs': jobs
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')