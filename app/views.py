from django.shortcuts import render,redirect, get_object_or_404
from .models import sample
from .resources import sampleResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.template import loader
import xlwt
from .forms import sampleform

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

def download(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Data')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['enrollmentno', 'name', 'branch','Fname', 'Mname', 'DOB', 'gender', 'category', 'subcategory', 'region',
                    'rank','allottedquota', 'allottedcategory', 'emailid', 'address', 'pcm', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    smp = sample.objects.all().values_list('enrollmentno', 'name', 'branch','Fname', 'Mname', 'DOB', 'gender', 'category', 'subcategory', 'region',
                    'rank','allottedquota', 'allottedcategory', 'emailid', 'address', 'pcm')
    for row in smp:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def sort(request):
    smp = sample.objects.order_by('rank')
    templ = loader.get_template('app/home.html')
    context = {
        'smp' : smp,
    }
    return HttpResponse(templ.render(context,request))

def quota_gn(request):
    smp = sample.objects.filter(category = 'GN').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))

def quota_obc(request):
    smp = sample.objects.filter(category = 'OBC').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))

def quota_sc(request):
    smp = sample.objects.filter(category = 'SC').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))

def quota_st(request):
    smp = sample.objects.filter(category = 'ST').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))

def gender_m(request):
    smp = sample.objects.filter(gender = 'Male').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))

def gender_f(request):
    smp = sample.objects.filter(gender = 'Female').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))

def branch_cse(request):
    smp = sample.objects.filter(branch = 'CSE').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))
def branch_it(request):
    smp = sample.objects.filter(branch = 'IT').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))
def branch_ece(request):
    smp = sample.objects.filter(branch = 'ECE').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))
def branch_eee(request):
    smp = sample.objects.filter(branch = 'EEE').values()
    if not smp:
        return HttpResponse('No records found')
    else:
        templ = loader.get_template('app/home.html')
        context = {
            'smp': smp,
        }
        return HttpResponse(templ.render(context, request))

def update(request,pk):
    order = sample.objects.get(id = pk)
    form = sampleform(instance= order)
    if request.method == "POST":
        form = sampleform(request.POST, instance= order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form" : form,
    }
    return render(request, 'app/update.html', context)

def delete(request, pk):
    order = sample.objects.get(id = pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order,}
    return render(request, 'app/delete.html', context)
