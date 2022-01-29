from django.contrib import admin
from software.models import Software
class SoftwareAdmin(admin.ModelAdmin):
    list_display=('software_title','software_tutorial_link','software_download_link')

admin.site.register(Software,SoftwareAdmin)
# Register your models here.
