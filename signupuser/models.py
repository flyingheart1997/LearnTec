from django.db import models
class Signupuser(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.IntegerField()
    country=models.CharField(max_length=60)
    

# Create your models here.
