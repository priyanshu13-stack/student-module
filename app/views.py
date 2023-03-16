from django.shortcuts import render,redirect, get_object_or_404
from .models import sample
from .resources import sampleResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.template import loader
import xlwt
import csv
from .forms import sampleform

def upload(request):
    smp = sample.objects.all()
    if (request.method == "POST"):
        sample_resource = sampleResource()
        dataset = Dataset()
        new_file = request.FILES['myfile']

        if not new_file.name.endswith('xlsx'):
            messages.info(request, 'File format not supported')
            return render(request, 'app/upload.html')

        imported_data = dataset.load(new_file.read(),format='xlsx')
        for i in imported_data:
            value = sample(
                i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],
                i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24],
            )
            value.save()
        return redirect('app:filter')
    
    context = {
        "smp" : smp,
    }
    return render(request, "app/upload.html", context)

def home(request):
    smp = sample.objects.all()
    context = {
        "smp" : smp,
    }
    
    return render(request, 'app/home.html', context)


def is_valid_query(param):
    return param!='' and param is not None


def filter(request):
    smp = sample.objects.all()
    if (smp.count() < 0):
        return redirect('app:upload')
    else:
        if request.method == "POST":
            srt = request.POST.get('sort')
            cat = request.POST.get('category')
            gen = request.POST.get('gender')
            br = request.POST.get('branch')
            re = request.POST.get('region')
            ty = request.POST.get('type')

            if is_valid_query(srt):
                if (srt == 'Increasing Order'):
                    smp = sample.objects.order_by('rank')

                elif (srt == 'Decreasing Order'):
                    smp = sample.objects.order_by('-rank')

            if is_valid_query(cat):
                if (cat == 'General'):
                    smp = sample.objects.filter(category = 'GN')

                elif (cat == 'OBC'):
                    smp = sample.objects.filter(category = 'OBC')

                elif (cat == 'SC'):
                    smp = sample.objects.filter(category = 'SC')

                elif (cat == 'ST'):
                    smp = sample.objects.filter(category = 'ST')

                elif (cat == 'EWS'):
                    smp = sample.objects.filter(category = 'EWS')

                elif (cat == 'AICTE'):
                    smp = sample.objects.filter(category = 'AICTE')


            if is_valid_query(gen):
                if (gen == 'Male'):
                    smp = sample.objects.filter(gender = 'MALE')
                
                elif (gen == 'Female'):
                    smp = sample.objects.filter(gender = 'FEMALE')

                elif (gen == 'Other'):
                    smp = sample.objects.filter(gender = 'OTHER')


            if is_valid_query(br):
                if (br == 'CSE'):
                    smp = sample.objects.filter(stream = 'CSE')
                
                elif (br == 'IT'):
                    smp = sample.objects.filter(stream = 'IT')
                
                elif (br == 'ECE'):
                    smp = sample.objects.filter(stream = 'ECE')

                elif (br == 'EEE'):
                    smp = sample.objects.filter(stream = 'EEE')


            if is_valid_query(re):
                if (re == 'Outside Delhi'):
                    smp = sample.objects.filter(region = 'OUTSIDE DELHI')

                elif (re == 'Delhi'):
                    smp = sample.objects.filter(region = 'DELHI')
                
            if is_valid_query(ty):
                if (ty == 'Regular'):
                    smp = sample.objects.filter(type = 'REGULAR')
                
                elif (ty == 'Upgraded Student'):
                    smp = sample.objects.filter(type = 'UPGRADE')

                elif (ty == 'Lateral Entry'):
                    smp = sample.objects.filter(type = 'LE')
                
                elif (ty == 'Management'):
                    smp = sample.objects.filter(type = 'MANAGEMENT')

    context = {
        "smp" : smp    
    }

    return render(request, "app/home.html", context)  
















def download(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Data')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['sno','enrollmentno', 'name', 'branch','Fname', 'Mname', 'DOB', 'gender', 'category', 'subcategory', 'region',
                    'rank','allottedquota', 'allottedcategory', 'emailid', 'address', 'pcm', ]
    for col_num in range(len(columns)): 
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    smp = sample.objects.all().values_list('sno','enrollmentno', 'name', 'branch','Fname', 'Mname', 'DOB', 'gender', 'category', 'subcategory', 'region',
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
            return redirect('app:filter')
        
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


def delete_all(request):
    s = sample.objects.all()
    s.delete()
    return redirect('app:upload')

def upload_new(request):
    return redirect('app:upload')


def validation1(self):
    if (self == True):
        return "YES"
    else:
        return "NO"

def download_file(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['SNo.', 'Type','Admitted', 'Enrollment Number', 'Name','Management','Year of Admission','IP Application Number','Father Name','Mother Name','Stream','DOB','Gender','Category','SubCategory','Region','Rank','Allotted Quota','Allotted Category','Student Mobile','Email ID','Father Mobile','Address','Aggregate','PCM'])

    smp = sample.objects.all()
    ind = 1

    for i in smp:
        writer.writerow([ind, i.type, validation1(i.admitted), i.enrollmentno, i.name,validation1(i.management),i.yearofadmission.strftime('%Y'),i.appno,i.Fname,i.Mname,i.stream,i.DOB.strftime('%d-%m-%Y'),i.gender,i.category,i.subcategory,i.region,i.rank,i.allottedquota,i.allottedcategory,i.studentmobile,i.emailid,i.fathermobile,i.address,i.aggregate,i.pcm])

        ind+=1

    return response