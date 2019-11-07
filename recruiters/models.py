from django.db import models

class Recruiter(models.Model):
    #class to set up recruiter variables to be added to the database when a new recruiter is added
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    bio = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    phone = models.TextField(max_length=20)
    def __str__(self):
        return self.name
