from django.db import models

# Create your models here.
class Mobile(models.Model):
    mobile_id=models.CharField(max_length=120,primary_key=True)
    mobile_name=models.CharField(max_length=120)
    brand=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    network=models.CharField(max_length=120)

