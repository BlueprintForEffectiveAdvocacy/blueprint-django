from django.contrib import admin

# Register your models here.
from main.models import Issue, Organization

admin.site.register(Issue)
admin.site.register(Organization)