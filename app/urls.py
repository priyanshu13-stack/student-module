from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload, name = "upload"),
    path('sort', views.sort, name = "sort"),
]
