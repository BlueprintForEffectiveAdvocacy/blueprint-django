from django.db import models

    
class Issue(models.Model):
    issue_name = models.CharField(max_length=64)
    summary = models.CharField(max_length=250)
    body = models.CharField(max_length=500)
    image = models.CharField(max_length=64)
    video = models.CharField(max_length=64)
    
class Organization(models.Model):
    org_name = models.CharField(max_length=64)
    issues = models.ManyToManyField(Issue)








