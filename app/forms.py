from .models import sample
from django import forms

class sampleform(forms.ModelForm):
    class Meta:
        model = sample
        fields = '__all__'
        widgets = {
            'sno': forms.TextInput(attrs={'class': 'form-control'}),
            'enrollmentno': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'appno': forms.TextInput(attrs={'class': 'form-control'}),
            'yearofadmission': forms.TextInput(attrs={'class': 'form-control'}),
            'Fname': forms.TextInput(attrs={'class': 'form-control'}),
            'Mname': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategory': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'allottedquota': forms.TextInput(attrs={'class': 'form-control'}),
            'allottedcategory': forms.TextInput(attrs={'class': 'form-control'}),
            'institute': forms.TextInput(attrs={'class': 'form-control'}),
            'emailid': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pcm': forms.TextInput(attrs={'class': 'form-control'}),
        }