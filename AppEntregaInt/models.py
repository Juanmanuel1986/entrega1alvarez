from django.db import models

# Create your models here.
class equipo(models.Model):
    nombre=models.CharField(max_length=100)
    nombreapp=models.CharField(max_length=100)

class unittest(models.Model):
    coverage=models.IntegerField()
    cantidadUT=models.IntegerField()

class regressiontest(models.Model):
    cantidadRT=models.IntegerField()

    
  