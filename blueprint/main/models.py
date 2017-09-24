from django.db import models

    
class Issue(models.Model):
    issue_name = models.CharField(max_length=64)
    scope = models.CharField(max_length=64, null=True, blank=True)
    summary = models.CharField(max_length=250, null=True, blank=True)
    body = models.CharField(max_length=500, null=True, blank=True)
    image = models.CharField(max_length=64, null=True, blank=True)
    video = models.CharField(max_length=64, null=True, blank=True)
    
class Organization(models.Model):
    org_name = models.CharField(max_length=64)
    issues = models.ManyToManyField(Issue)








