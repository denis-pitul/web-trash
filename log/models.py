from django.db import models

# Create your models here.
class Entry(models.Model):
    date = models.DateTimeField('date published')
    text = models.CharField(max_length = 5000)
