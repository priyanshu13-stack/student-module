from django.db import models

class sample(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100, blank= True)

    def __str__(self):
        return self.name