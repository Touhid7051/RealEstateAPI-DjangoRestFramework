from django.contrib import admin

# Register your models here.

from contact.models import Contact

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact)