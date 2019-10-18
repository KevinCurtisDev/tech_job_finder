from django.contrib import admin

from .models import Recruiter

class RecruiterAdmin(admin.ModelAdmin):
    # Add fields to the admin Recruiter area
    list_display = ('id', 'name', 'email')
    # Make the the recruiter ID and Name a clickable link
    list_display_links = ('id', 'name')
    # Add pagination to admin recruiter listing
    list_per_page = 10

admin.site.register(Recruiter, RecruiterAdmin)
