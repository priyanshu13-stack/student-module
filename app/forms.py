from .models import sample
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class sampleform(forms.ModelForm):
    class Meta:
        model = sample
        management =  forms.BooleanField()
        admitted = forms.BooleanField()
        fields = '__all__'
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'enrollmentno': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'yearofadmission': forms.TextInput(attrs={'class': 'form-control'}),
            'appno': forms.TextInput(attrs={'class': 'form-control'}),
            'Fname': forms.TextInput(attrs={'class': 'form-control'}),
            'Mname': forms.TextInput(attrs={'class': 'form-control'}),
            'stream': forms.Select(attrs={'class': 'form-control'}),
            'DOB': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'allottedquota': forms.Select(attrs={'class': 'form-control'}),
            'allottedcategory': forms.Select(attrs={'class': 'form-control'}),
            'studentmobile': forms.TextInput(attrs={'class': 'form-control'}),
            'emailid': forms.TextInput(attrs={'class': 'form-control'}),
            'fathermobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'aggregate': forms.TextInput(attrs={'class': 'form-control'}),
            'pcm': forms.TextInput(attrs={'class': 'form-control'}),
        }
