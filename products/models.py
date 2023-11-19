from django.db import models
from datetime import datetime
# Create your models here.
class Car(models.Model):
    x = [
        ('phones', 'phones')
    ]
    name =  models.CharField(max_length=50, default='post')
    description = models.TextField(null =True, blank = True,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default ='photos/23/10/31/Bricks.png', height_field=None, width_field=None, max_length=None)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null =True, blank = True, choices = x)

    def __str__(self):
        return self.name

class Test(models.Model):
    date = models.DateField(null = True)
    time = models.TimeField(null = True)
    current = models.DateTimeField(default = datetime.now)