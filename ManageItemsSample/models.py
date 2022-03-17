from django.db import models

# Create your models here.
class sampleitems(models.Model):
    sItem = models.SmallIntegerField(primary_key=True)
    sName = models.CharField(max_length=50)
    sDescription = models.TextField(max_length=200)
    sQty = models.SmallIntegerField