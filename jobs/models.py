from django.db import models
from datetime import datetime
from recruiters.models import Recruiter

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)
    description = models.TextField(max_length=800)
    salary = models.IntegerField()
    listed_date = models.DateTimeField(default=datetime.now, blank=True)
    added = models.BooleanField(default=True)
    def __str__(self):
        return self.title

