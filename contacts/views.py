from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        job_id = request.POST['job_id']
        job = request.POST['job']
        name = request.POST['name']
        email = request.POST['email']
        user_id = request.POST['user_id']
        message = request.POST['message']
        recruiter_email = request.POST['recruiter_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(job_id=job_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already enquired about this job')
                return redirect('/jobs/'+job_id)

        contact = Contact(job=job, job_id=job_id, name=name, email=email, user_id=user_id, message=message)

        contact.save()

        messages.success(request, 'Your query has been sent')
        return redirect('/jobs/'+job_id)