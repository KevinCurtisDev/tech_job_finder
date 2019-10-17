from django.shortcuts import render

def index(request):
    return render(request, 'jobs/jobs.html')


def job(request):
    return render(request, 'jobs/job.html')


def search(request):
    return render(request, 'jobs/search.html')
