from django.shortcuts import render,redirect, get_object_or_404
from .models import sample
from .resources import sampleResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.template import loader


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
                i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],
                i[17],i[18],i[19],
            )
            value.save()
    context = {
        "smp" : smp,
    }

    return render(request, 'app/home.html', context)

def sort(request):
    smp = sample.objects.order_by('rank')
    templ = loader.get_template('app/home.html')
    context = {
        'smp' : smp,
    }
    return HttpResponse(templ.render(context,request))

def quota(request):
    my = sample.objects.values_list('category')
    templ = loader.get_template('app/home.html')
    context = {
        'my': my,
    }
    return HttpResponse(templ.render(context, request))

