from django.db import models


class PageContent(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=250)
    body = models.CharField(max_length=500)
    image = models.CharField(max_length=64)
    video = models.CharField(max_length=64)
    
class Issue(models.Model):
    issue_name = models.CharField(max_length=64)
    page_content = models.OneToOneField(
        PageContent,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
class Organization(models.Model):
    org_name = models.CharField(max_length=64)
    issues = models.ManyToManyField(Issue)






