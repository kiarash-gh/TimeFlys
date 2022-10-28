from operator import mod
from statistics import mode
from django.db import models

class Discription(models.Model):
    discription = models.TextField(null=True, blank=True)
    


class People(models.Model):
    picture = models.ImageField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    linkedin_url = models.URLField(blank=True, null=True)
    web_url = models.URLField(blank=True, null=True)
    job_title = models.CharField(max_length=255)
    discription = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.firstname.title()} {self. lastname.title()}'