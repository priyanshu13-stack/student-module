from django.db import models

allotedquotachoices = (
    ('HS', 'HS'),
    ('OS', 'OS'),
    ('AI', 'AI'),
)

allottedcategorychoices = (
    ('OPNO','OPNO'),
    ('SCNO', 'SCNO'),
    ('NODF','NODF'),
)

subcategorychoices = (
    ('DEFENCE','DEFENCE'),
    ('JAIN', 'JAIN'),
    ('MUSLIM','MUSLIM'),
    ('SIKH','SIKH'),
    ('PWD','PWD'),
    ('JK','JK'),
)

regionchoices = (
    ('DELHI', 'DELHI'),
    ('OUTSIDE DELHI', 'OUTSIDE DELHI'),
)

categorychoices = (
    ('GN','GN'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    ('OBC', 'OBC'),
    ('EWS', 'EWS'),
    ('AICTE', 'AICTE'),
)

genderchoices = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER'),
)

typechoices = (
    ('REGULAR', 'REGULAR'),
    ('UPGRADED', 'UPGRADED'),
    ('LE', 'LE'),
    ('MANAGEMENT', 'MANAGEMENT'),
)

streamchoices = (
    ('CSE','CSE'),
    ('IT','IT'),
    ('ECE','ECE'),
    ('EEE','EEE'),
)

admittedchoices = (
    ('YES', 'YES'),
    ('NO', 'NO'),
)

managementchoices = (
    ('YES', 'YES'),
    ('NO', 'NO'),
)

class sample(models.Model):
    type = models.CharField(max_length=10, choices= typechoices ,default='Regular')
    admitted = models.CharField(max_length=50, default= '',null= True, choices= admittedchoices)
    enrollmentno = models.IntegerField(null = True, default = None , blank=True, unique = True)
    name = models.CharField(max_length=100, default=False)
    management = models.CharField(max_length=50, default = '', null= True, choices= managementchoices)
    yearofadmission = models.DateTimeField(default=False)
    appno = models.CharField(default= "", max_length=200, unique= True)
    Fname = models.CharField(max_length=200, default=False)
    Mname = models.CharField(max_length=200, default=False)
    stream = models.CharField(max_length=200, choices= streamchoices,default=False)
    DOB = models.DateField(default=False)
    gender = models.CharField(max_length=50,choices= genderchoices ,default=False)
    category = models.CharField(max_length=5,choices= categorychoices ,default=False)
    subcategory = models.CharField(max_length=10, choices= subcategorychoices ,default=False)
    region = models.CharField(max_length=50,choices= regionchoices ,default=False)
    rank = models.IntegerField(null = True, default=None , blank=True)
    allottedquota = models.CharField(max_length=10,choices= allotedquotachoices, default=False)
    allottedcategory = models.CharField(max_length=10,choices= allottedcategorychoices, default=False)
    studentmobile = models.IntegerField(null = True, default=None , blank=True)
    emailid = models.EmailField(max_length=200, default='')
    fathermobile = models.IntegerField(null = True, default=None , blank=True)
    address = models.CharField(max_length=200, default=False)
    aggregate = models.FloatField(null = True, default=None , blank=True)
    pcm = models.FloatField(null = True, default=None , blank=True)

    def __str__(self):
        return self.name
    def yearpub(self):
        return self.yearofadmission.strftime('%Y')

    def dateofbirth(self):
        return self.DOB.strftime('%d-%m-%Y')

    def admitted_yn(self):
        if (self.admitted == "YES"):
            return "YES"
        else:
            return "NO"

    def management_yn(self):
        if (self.management == "YES"):
            return "YES"
        else:
            return "NO"
