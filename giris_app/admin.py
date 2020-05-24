from django.contrib import admin
from django.http import HttpResponse
from .models import universite
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class UnvResource(resources.ModelResource):

    class Meta:
        model = universite


class UnvAdmin(ImportExportModelAdmin):
    resource_class = UnvResource

      

# Register your models here.

# admin.site.register(universite)
admin.site.register(universite, UnvAdmin)  