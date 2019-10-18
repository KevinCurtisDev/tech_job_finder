from django.shortcuts import render

from .models import Job

def index(request):
    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }

    return render(request, 'jobs/jobs.html', context)


def job(request, job_id):
    return render(request, 'jobs/job.html')


def search(request):
    return render(request, 'jobs/search.html')
