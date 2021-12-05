from django.db import models
# Create your models here.
class Medio(models.Model):
    
    type_options = [
        ('Debit Card', 'Debit Card'),
        ('Credit Card','Credit Card')
    ]
    
    id      = models.BigAutoField(primary_key=True)
    userId  = models.CharField('userId',blank=False, max_length=255)
    type    = models.CharField('type',choices=type_options,max_length=50,blank=False)
    number  = models.CharField('number', max_length=50,blank=False)
    expDate = models.DateField('expDate',auto_created=False, blank=False)
    cv      = models.CharField('cv', max_length=3,blank=False)

