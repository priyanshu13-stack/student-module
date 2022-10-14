from django.shortcuts import render,redirect, get_object_or_404
from .models import sample
from .resources import sampleResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def home(request):
    return render(request, "app/home.html")

def upload(request):
    smp = sample.objects.all()
    if request.method == "POST":
        sample_resource = sampleResource()
        dataset = Dataset()
        new_file = request.FILES['myfile']

        if not new_file.name.endswith('xlsx'):
            messages.info(request, 'File format not supported')
            return render(request, 'app/home.html')

        imported_data = dataset.load(new_file.read(),format='xlsx')
        for i in imported_data:
            value = sample(
                i[0],
                i[1],
                i[2],
                i[3]
            )
            value.save()

    context = {
        "smp" : smp,
    }

    return render(request, 'app/home.html', context)

def delete(request):
    if request.method == "POST":
        smp = sample.objects.all()
        smp.delete()

    return render(request, "app/home.html")