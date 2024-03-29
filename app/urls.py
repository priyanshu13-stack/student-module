from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.filter, name = "filter"),
    path('upload', views.upload, name = "upload"),
    path('deleteall', views.delete_all, name = "deleteall"),
    path('upload_new', views.upload_new, name = "upload_new"),
    path('home/', views.home, name = "home"),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
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
    path('download_file', views.download_file, name="download_file"),
    path('upload_enroll', views.upload_enroll, name = "upload_enroll"),
    path('show_enroll', views.show_enroll, name = "show_enroll"),
]
