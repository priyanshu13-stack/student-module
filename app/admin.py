from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import sample

@admin.register(sample)
class sampleAdmin(ImportExportModelAdmin):
    list_display = ('enrollmentno', 'name', 'branch','Fname', 'Mname', 'DOB', 'gender', 'category', 'subcategory', 'region',
                    'rank','allottedquota', 'allottedcategory', 'emailid', 'address', 'pcm')

