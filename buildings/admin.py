from django.contrib import admin

# Register your models here.

from buildings.models import Home,ImageFiles

admin.site.register(Home)
admin.site.register(ImageFiles)