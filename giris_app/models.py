from django.db import models

# Create your models here.
class universite(models.Model):
      adi =models.CharField(max_length=1000)
      sehir =models.CharField(max_length=50)
      ulke  = models.CharField(max_length=100)

      