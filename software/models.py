from django.db import models
class Software(models.Model):
    software_title=models.CharField(max_length=50)
    software_tutorial_link=models.CharField(max_length=200)
    software_download_link=models.CharField(max_length=200)

# Create your models here.
