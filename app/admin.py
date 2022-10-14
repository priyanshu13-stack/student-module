from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import sample

@admin.register(sample)
class sampleAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'location')
