from import_export import resources
from .models import sample

class sampleResource(resources.ModelResource):
    class meta:
        model = sample