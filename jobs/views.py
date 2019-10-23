from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator

from .models import Job

def index(request):
    # set job variable to hold job info from database (ordered by date)
    jobs = Job.objects.order_by('-listed_date')

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
    # SEt job variable to return the job data or a 404 if job id does not exist
    job = get_object_or_404(Job, pk=job_id)

    context = {
        'job': job
    }
    # return a dynamically created url for individual job listings
    return render(request, 'jobs/job.html', context)


def search(request):
    query = Job.objects.order_by('-listed_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query = query.filter(title__icontains=keywords)

    context = {
        'jobs': query
    }


    return render(request, 'jobs/search.html', context)
