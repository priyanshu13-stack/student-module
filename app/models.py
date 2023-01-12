from django.db import models

allotedquotachoices = (
    ('opno','OPNO'),
    ('scno', 'SCNO'),
    ('stno','STNO'),
    ('nodf','NODF'),
    ('noph','NOPH'),
)

allottedcategorychoices = (
    ('hs', 'HS'),
    ('os', 'OS'),
    ('ai', 'AI'),
)

subcategorychoices = (
    ('defence','DEFENCE'),
    ('jain', 'JAIN'),
    ('muslim','MUSLIM'),
    ('sikh','SIKH'),
    ('pwd','PWD'),
    ('jk','JK'),
)

regionchoices = (
    ('delhi', 'DELHI'),
    ('outside delhi', 'OUTSIDE DELHI'),
)

categorychoices = (
    ('gen', 'GEN'),
    ('sc', 'SC'),
    ('st', 'ST'),
    ('obc', 'OBC'),
    ('ews', 'EWS'),
    ('aicte', 'AICTE'),
)

genderchoices = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER'),
)

typechoices = (
    ('regular', 'REGULAR'),
    ('upgraded', 'UPGRADED'),
    ('le', 'LE'),
)

streamchoices = (
    ('cse','CSE'),
    ('it','IT'),
    ('ece','ECE'),
    ('eee','EEE'),
)
class sample(models.Model):
    type = models.CharField(max_length=10, choices= typechoices ,default='Regular')
    admitted = models.BooleanField(default=False)
    enrollmentno = models.IntegerField(null = True, default=None , blank=True)
    name = models.CharField(max_length=100, default=False)
    management = models.BooleanField(default = False)
    yearofadmission = models.DateTimeField(default=False)
    appno = models.CharField(default=False, max_length=200)
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
    emailid = models.EmailField(max_length=20, default='')
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
        if (self.admitted == True):
            return "YES"
        else:
            return "NO"

    def management_yn(self):
        if (self.management == True):
            return "YES"
        else:
            return "NO"
