from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import sample

@admin.register(sample)

class sampleAdmin(ImportExportModelAdmin):
    list_display = ('type','admitted','enrollmentno', 'name', 'management', 'yearofadmission', 'appno','Fname', 'Mname','stream' ,'DOB', 'gender', 'category', 'subcategory', 'region',
                    'rank','allottedquota', 'allottedcategory','studentmobile' ,'emailid','fathermobile' ,'address','aggregate', 'pcm')
    pass

