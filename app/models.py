from django.db import models

class sample(models.Model):
    sno = models.IntegerField(null = False, default=None, blank= False)
    enrollmentno = models.IntegerField(null = True, default=None , blank=True)
    name = models.CharField(max_length=100, default=False)
    branch = models.CharField(max_length=200, default=False)
    appno = models.CharField(default=False , max_length=200)
    yearofadmission = models.DateField(default= False)
    Fname = models.CharField(max_length=200, default=False)
    Mname = models.CharField(max_length=200, default=False)
    DOB = models.DateField(default=False)
    gender = models.CharField(max_length=50, default=False)
    category = models.CharField(max_length=5, default=False)
    subcategory = models.CharField(max_length=10, default=False)
    region = models.CharField(max_length=50, default=False)
    rank = models.IntegerField(null = True, default=None , blank=True)
    allottedquota = models.CharField(max_length=10, default=False)
    allottedcategory = models.CharField(max_length=10, default=False)
    institute = models.CharField(max_length=200, default=False)
    emailid = models.EmailField(max_length=100, default=False)
    address = models.CharField(max_length=200, default=False)
    pcm = models.FloatField(null = True, default=None , blank=True)

    def __str__(self):
        return self.name