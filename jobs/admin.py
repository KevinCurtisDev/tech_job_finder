from django.contrib import admin

from .models import Job

class JobAdmin(admin.ModelAdmin):
    # Add fields to the admin job area
    list_display = ('id', 'title', 'recruiter')
    # Make the the job ID and Title a clickable link
    list_display_links = ('id', 'title')
    # Add pagination to admin job listing
    list_per_page = 10

admin.site.register(Job, JobAdmin)
