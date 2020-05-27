from django.contrib import admin
from django.http import HttpResponse
from .models import universite
from import_export.admin import ImportExportModelAdmin
      
class UnvAdmin(ImportExportModelAdmin):
    resource_class = universite
# Register your models here.

# admin.site.register(universite)
admin.site.register(universite, UnvAdmin)  


