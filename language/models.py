from django.db import models
class Language(models.Model):
    language_title=models.CharField(max_length=50)
    language_desc=models.TextField()
    language_tutorial_link=models.CharField(max_length=200)
    language_video_link=models.CharField(max_length=200)
# Create your models here.