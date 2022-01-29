from django.contrib import admin
from signupuser.models import Signupuser
class SignupuserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','country')

admin.site.register(Signupuser,SignupuserAdmin)
# Register your models here.
