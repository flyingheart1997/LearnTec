from django.contrib import admin
from language.models import Language
class LanguageAdmin(admin.ModelAdmin):
    list_display=('language_title','language_desc','language_tutorial_link','language_video_link')

admin.site.register(Language,LanguageAdmin)
# Register your models here.
