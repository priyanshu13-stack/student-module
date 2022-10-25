from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload, name = "upload"),
    path('sort', views.sort, name = "sort"),
    path('quota_gn', views.quota_gn, name = "quota_gn"),
    path('quota_obc', views.quota_obc, name = "quota_obc"),
    path('quota_sc', views.quota_sc, name = "quota_sc"),
    path('quota_st', views.quota_st, name = "quota_st"),
    path('gender_m', views.gender_m, name = "gender_m"),
    path('gender_f', views.gender_f, name = "gender_f"),
    path('branch_cse', views.branch_cse, name = "branch_cse"),
    path('branch_it', views.branch_it, name = "branch_it"),
    path('branch_ece', views.branch_ece, name = "branch_ece"),
    path('branch_eee', views.branch_eee, name = "branch_eee"),
    path(r'^download/$', views.download, name = "download"),
]
