from django.db import models


# Create your models here.

class Job(models.Model):
    objects = None
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=300)

    def __str__(self):
       
        return self.summary
