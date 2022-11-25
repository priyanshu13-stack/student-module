from django.forms import ModelForm
from .models import sample

class sampleform(ModelForm):
    class Meta:
        model = sample
        fields = '__all__'