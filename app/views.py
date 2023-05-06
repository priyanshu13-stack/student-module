from django.shortcuts import render,redirect, get_object_or_404
from .models import sample
from django.utils.datastructures import MultiValueDictKeyError
from .resources import sampleResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
import xlwt
import csv
import json
from django.db import IntegrityError
from .forms import sampleform

def upload(request):
    smp = sample.objects.all()
    if (request.method == "POST" and request.FILES['myfile']):
            sample_resource = sampleResource()
            new_file = request.FILES['myfile']

            if new_file.name.endswith('.xlsx') or new_file.name.endswith('.xls'):
                dataset = Dataset()

                imported_data = dataset.load(new_file.read(),format='xlsx')
                for i in imported_data:
                    id = i[0]
                    type = i[1]
                    admitted = i[2]
                    enrollmentno = i[3]
                    name = i[4]
                    management= i[5]
                    yearofadmission= i[6]
                    appno= i[7]
                    Fname= i[8]
                    Mname= i[9]
                    stream= i[10]
                    DOB= i[11]
                    gender= i[12]
                    category = i[13]
                    subcategory= i[14]
                    region= i[15]
                    rank= i[16]
                    allottedquota = i[17]
                    allottedcategory= i[18]
                    studentmobile= i[19]
                    emailid= i[20]
                    fathermobile= i[21]
                    address= i[22]
                    aggregate= i[23]
                    pcm = i[24]

                    try:
                        # if unique values exist in the database or not 
                        existing_record = sample.objects.get(enrollmentno = enrollmentno, appno = appno)
                    
                    except sample.DoesNotExist:
                        sample.objects.create(id = id, type = type , admitted = admitted, enrollmentno = enrollmentno, name = name, management = management, yearofadmission = yearofadmission, appno = appno, Fname = Fname, Mname = Mname, stream = stream, DOB = DOB, gender = gender, category = category, subcategory = subcategory, region = region, rank = rank, allottedquota = allottedquota, allottedcategory = allottedcategory, studentmobile = studentmobile, emailid = emailid, fathermobile = fathermobile, address = address, aggregate = aggregate, pcm = pcm)

                    else:
                        if existing_record.id != id or existing_record.type != type or existing_record.admitted != admitted or existing_record.name != name or existing_record.management != management or existing_record.yearofadmission !=yearofadmission or existing_record.Fname != Fname or existing_record.Mname != Mname or existing_record.stream != stream or existing_record.DOB != DOB or existing_record.gender != gender or existing_record.category != category or existing_record.subcategory != subcategory or existing_record.region != region or existing_record.rank != rank or existing_record.allottedquota != allottedquota or existing_record.allottedcategory != allottedcategory or existing_record.studentmobile != studentmobile or existing_record.emailid != emailid or existing_record.fathermobile != fathermobile or existing_record.address!= address or existing_record.aggregate!= aggregate or existing_record.pcm!= pcm :

                            existing_record.id = id
                            existing_record.type = type
                            existing_record.admitted = admitted
                            existing_record.enrollmentno = enrollmentno
                            existing_record.name = name
                            existing_record.management = management
                            existing_record.yearofadmission =yearofadmission
                            existing_record.appno = appno
                            existing_record.Fname = Fname
                            existing_record.Mname = Mname
                            existing_record.stream = stream
                            existing_record.DOB = DOB
                            existing_record.gender = gender
                            existing_record.category = category
                            existing_record.subcategory = subcategory
                            existing_record.region = region
                            existing_record.rank = rank
                            existing_record.allottedquota = allottedquota
                            existing_record.allottedcategory = allottedcategory
                            existing_record.studentmobile = studentmobile
                            existing_record.emailid = emailid
                            existing_record.fathermobile = fathermobile
                            existing_record.address= address
                            existing_record.aggregate= aggregate
                            existing_record.pcm= pcm
                            try:
                                existing_record.save()
                            except IntegrityError as e:
                                pass
                return redirect('app:filter')
    else:
        return render(request, "app/upload.html")
            

# def upload_enroll(request):
#     smp = sample.objects.all()
#     if (request.method == "POST"):
#         try:
#             sample_resource = sampleResource()
#             dataset = Dataset()
#             new_file = request.FILES['enrollfile']

#             if not new_file.name.endswith('xlsx'):
#                 messages.info(request, 'File format not supported')
#                 return render(request, 'app/upload.html')

#             imported_data = dataset.load(new_file.read(),format='xlsx')
#             for i in imported_data:
#                 value = sample(
#                     i[0],i[1],i[2],
#                 )
#                 value.save()
#             return redirect('app:filter')
#         except MultiValueDictKeyError:
#             return redirect('app:upload')
#         except IntegrityError as e :
#             return HttpResponseBadRequest("Data already exists. Try uploading another file!")

    
#     context = {
#         "smp" : smp,
#     }
#     return render(request, "app/upload.html", context)


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
            alq = request.POST.get('aq')
            alc = request.POST.get('ac')

            if is_valid_query(srt):
                if (srt == 'Increasing Order'):
                    smp = smp.order_by('rank')

                elif (srt == 'Decreasing Order'):
                    smp = smp.order_by('-rank')

            if is_valid_query(cat):
                if (cat == 'General'):
                    smp = smp.filter(category = 'GN')

                elif (cat == 'OBC'):
                    smp = smp.filter(category = 'OBC')

                elif (cat == 'SC'):
                    smp = smp.filter(category = 'SC')

                elif (cat == 'ST'):
                    smp = smp.filter(category =  'ST')

                elif (cat == 'EWS'):
                    smp = smp.filter(category = 'EWS')

                elif (cat == 'AICTE'):
                    smp = smp.filter(category = 'AICTE')


            if is_valid_query(gen):
                if (gen == 'Male'):
                    smp = smp.filter(gender = 'MALE')
                
                elif (gen == 'Female'):
                    smp = smp.filter(gender = 'FEMALE')

                elif (gen == 'Other'):
                    smp = smp.filter(gender = 'OTHER')


            if is_valid_query(br):
                if (br == 'CSE'):
                    smp = smp.filter(stream = 'CSE')
                
                elif (br == 'IT'):
                    smp = smp.filter(stream = 'IT')
                
                elif (br == 'ECE'):
                    smp = smp.filter(stream = 'ECE')

                elif (br == 'EEE'):
                    smp = smp.filter(stream = 'EEE')


            if is_valid_query(re):
                if (re == 'Outside Delhi'):
                    smp = smp.filter(region = 'OUTSIDE DELHI')

                elif (re == 'Delhi'):
                    smp = smp.filter(region = 'DELHI')
                
            if is_valid_query(ty):
                if (ty == 'Regular'):
                    smp = smp.filter(type = 'REGULAR')
                
                elif (ty == 'Upgraded Student'):
                    smp = smp.filter(type = 'UPGRADE')

                elif (ty == 'Lateral Entry'):
                    smp = smp.filter(type = 'LE')
                
                elif (ty == 'Management Student'):
                    smp = smp.filter(management = 'YES')

                elif (ty == 'Non-Management Student'):
                    smp = smp.filter(management = 'NO')

            if is_valid_query(alq):
                if (alq == 'HS'):
                    smp = smp.filter(allottedquota = "HS")
                
                elif (alq == 'OS'):
                    smp = smp.filter(allottedquota = "OS")

                elif (alq == 'AI'):
                    smp = smp.filter(allottedquota = "AI")

            if is_valid_query(alc):
                if (alc == 'OPNO'):
                    smp = smp.filter(allottedcategory = "OPNO")
                
                elif (alc == 'SCNO'):
                    smp = smp.filter(allottedcategory = "SCNO")
                
                elif (alc == 'NODF'):
                    smp = smp.filter(allottedcategory = "NODF")

    context = {
        "smp" : smp    
    }
    
    return render(request, "app/home.html", context)  



def download_file(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['SNo.', 'Type','Admitted', 'Enrollment Number', 'Name','Management','Year of Admission','IP Application Number','Father Name','Mother Name','Stream','DOB','Gender','Category','SubCategory','Region','Rank','Allotted Quota','Allotted Category','Student Mobile','Email ID','Father Mobile','Address','Aggregate','PCM'])

    smp = sample.objects.all()
    if request.method == "POST":
            srt = request.POST.get('sort')
            cat = request.POST.get('category')
            gen = request.POST.get('gender')
            br = request.POST.get('branch')
            re = request.POST.get('region')
            ty = request.POST.get('type')
            alq = request.POST.get('aq')
            alc = request.POST.get('ac')

            if is_valid_query(srt):
                if (srt == 'Increasing Order'):
                    smp = smp.order_by('rank')

                elif (srt == 'Decreasing Order'):
                    smp = smp.order_by('-rank')

            if is_valid_query(cat):
                if (cat == 'General'):
                    smp = smp.filter(category = 'GN')

                elif (cat == 'OBC'):
                    smp = smp.filter(category = 'OBC')

                elif (cat == 'SC'):
                    smp = smp.filter(category = 'SC')

                elif (cat == 'ST'):
                    smp = smp.filter(category =  'ST')

                elif (cat == 'EWS'):
                    smp = smp.filter(category = 'EWS')

                elif (cat == 'AICTE'):
                    smp = smp.filter(category = 'AICTE')


            if is_valid_query(gen):
                if (gen == 'Male'):
                    smp = smp.filter(gender = 'MALE')
                
                elif (gen == 'Female'):
                    smp = smp.filter(gender = 'FEMALE')

                elif (gen == 'Other'):
                    smp = smp.filter(gender = 'OTHER')


            if is_valid_query(br):
                if (br == 'CSE'):
                    smp = smp.filter(stream = 'CSE')
                
                elif (br == 'IT'):
                    smp = smp.filter(stream = 'IT')
                
                elif (br == 'ECE'):
                    smp = smp.filter(stream = 'ECE')

                elif (br == 'EEE'):
                    smp = smp.filter(stream = 'EEE')


            if is_valid_query(re):
                if (re == 'Outside Delhi'):
                    smp = smp.filter(region = 'OUTSIDE DELHI')

                elif (re == 'Delhi'):
                    smp = smp.filter(region = 'DELHI')
                
            if is_valid_query(ty):
                if (ty == 'Regular'):
                    smp = smp.filter(type = 'REGULAR')
                
                elif (ty == 'Upgraded Student'):
                    smp = smp.filter(type = 'UPGRADE')

                elif (ty == 'Lateral Entry'):
                    smp = smp.filter(type = 'LE')
                
                elif (ty == 'Management Student'):
                    smp = smp.filter(management = True)

                elif (ty == 'Non-Management Student'):
                    smp = smp.filter(management = False)

            if is_valid_query(alq):
                if (alq == 'HS'):
                    smp = smp.filter(allottedquota = "HS")
                
                elif (alq == 'OS'):
                    smp = smp.filter(allottedquota = "OS")

                elif (alq == 'AI'):
                    smp = smp.filter(allottedquota = "AI")

            if is_valid_query(alc):
                if (alc == 'OPNO'):
                    smp = smp.filter(allottedcategory = "OPNO")
                
                elif (alc == 'SCNO'):
                    smp = smp.filter(allottedcategory = "SCNO")
                
                elif (alc == 'NODF'):
                    smp = smp.filter(allottedcategory = "NODF")


    ind = 1

    for i in smp:
        writer.writerow([ind, i.type, validation1(i.admitted), i.enrollmentno, i.name,validation1(i.management),i.yearofadmission.strftime('%Y'),i.appno,i.Fname,i.Mname,i.stream,i.DOB.strftime('%d-%m-%Y'),i.gender,i.category,i.subcategory,i.region,i.rank,i.allottedquota,i.allottedcategory,i.studentmobile,i.emailid,i.fathermobile,i.address,i.aggregate,i.pcm])

        ind+=1

    return response















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

