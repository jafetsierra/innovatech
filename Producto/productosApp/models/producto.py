from django.db import models

# Create your models here.
class Producto(models.Model):
    id          = models.BigAutoField(primary_key=True)
    name        = models.CharField('name', max_length=100)
    description = models.CharField('description', max_length=250)
    price       = models.FloatField()
    category    = models.CharField('category',max_length=50)
    #thumbnail   = models.ImageField()
    stock       = models.IntegerField(default=0)
    