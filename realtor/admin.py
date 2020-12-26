from django.contrib import admin

# Register your models here.
from realtor.models import Agent

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Agent)