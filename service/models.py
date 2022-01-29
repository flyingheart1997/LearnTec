from django.db import models
class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_desc=models.TextField()
    service_link=models.CharField(max_length=200)

# Create your models here.
