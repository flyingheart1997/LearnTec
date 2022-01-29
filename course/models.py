from django.db import models
class Course(models.Model):
    course_icon=models.CharField(max_length=50)
    course_title=models.CharField(max_length=50)
    course_desc=models.TextField()
    course_tutorial_link=models.CharField(max_length=200)
    course_video_link=models.CharField(max_length=200)
# Create your models here.
