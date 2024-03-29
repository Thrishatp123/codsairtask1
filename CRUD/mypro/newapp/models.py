from django.db import models

# Create your models here.
class Member(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)

