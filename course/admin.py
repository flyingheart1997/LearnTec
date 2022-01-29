from django.contrib import admin
from course.models import Course
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_icon','course_title','course_desc','course_tutorial_link','course_video_link')

admin.site.register(Course,CourseAdmin)

# Register your models here.
