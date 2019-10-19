from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator

from .models import Job

def index(request):
    # set job variable to hold job info from database
    jobs = Job.objects.all()

    # set nuber of jobs to be listed per page 
    paginator = Paginator(jobs, 2)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)

    # context variable holds data to be inserted into the html markup
    context = {
        'jobs': paged_jobs
    }

    # return the jobs markup and make available the database job data
    return render(request, 'jobs/jobs.html', context)


def job(request, job_id):
    # return a dynamically created url for individual job listings
    return render(request, 'jobs/job.html')


def search(request):
    return render(request, 'jobs/search.html')
