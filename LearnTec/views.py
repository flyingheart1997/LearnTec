from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from course.models import Course
from service.models import Service
from language.models import Language
from software.models import Software
from signupuser.models import Signupuser

def homepage(request):
    servicesData=Service.objects.all()
    if request.method=="GET":
        search_item=request.GET.get('search')
        if search_item!=None:
            servicesData=Service.objects.filter(service_title__contains=search_item)
    data={
        'servicesData':servicesData
    }
    return render(request,"index.html",data)

def courses(request):
    courseData=Course.objects.all()
    if request.method=="GET":
        search_item=request.GET.get('search')
        if search_item!=None:
            courseData=Course.objects.filter(course_title__contains=search_item)

    data={
        'courseData':courseData
    }
    return render(request,"courses.html",data)    

def language(request):
    languageData=Language.objects.all()
    if request.method=="GET":
        search_item=request.GET.get('search')
        if search_item!=None:
            languageData=Language.objects.filter(language_title__contains=search_item)
    data={
        'languageData':languageData
    }
    return render(request,"language.html",data)    

def software(request):
    softwareData=Software.objects.all()
    if request.method=="GET":
        search_item=request.GET.get('search')
        if search_item!=None:
            softwareData=Software.objects.filter(software_title__contains=search_item)
    data={
        'softwareData':softwareData
    }
    return render(request,"env.html",data)

def enroll(request):
    if request.method=="POST":
        name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        country=request.POST.get('country')
        data=Signupuser(first_name=name,last_name=last_name,email=email,phone=phone,country=country)
        try:
            Signupuser._default_manager.get(email=email,phone=phone)
            return redirect("/home")
        except data.DoesNotExist:
            data.save() 
            return redirect("/home")
       
    return render(request,"sgnup.html")


