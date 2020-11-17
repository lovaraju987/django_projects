from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name = models.CharField(max_length=101)
    img = models.ImageField(upload_to='pics')
    like = models.IntegerField()
    comment = models.IntegerField()
    description = models.TextField()