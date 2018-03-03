from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import course,course1,message

# Create your views here.
def index(request):
    all_courses = course.objects.all().filter(user__email=request.user.email)
    #all_courses=course.objects.all()
    context={
        'all_courses':all_courses
    }
    return render(request,'moodle_prof_index.html', context)

def course_add(request):
    if request.method == "POST":
        courset=course()
        courset1=course1()
        courset.course_name = request.POST.get('name')
        courset.course_code = request.POST.get('code')
        courset1.course_name = courset.course_name
        courset1.course_code = courset.course_code
        courset.user=request.user
        courset.save()
        courset1.save()

    return render(request,'course_add.html')

def course_drop(request):
    if request.method=="POST":
        courset=course.objects.all().filter(course_code=request.POST.get('code'))
        courset1=course1.objects.all().filter(course_code=request.POST.get('code'))
        courset.delete()
        courset1.delete()
    return render(request,'course_drop_prof.html')

def message_add(request):
    if request.method=="POST":
        Message=message()
        courset1=course1.objects.all().get(course_code=request.POST.get('code'))
        Message.message=request.POST.get('message')
        Message.course= courset1
        Message.save()

        users = courset1.user.all()
        for usersp in users:
            Message.user.add(usersp)
    return render(request,'message_add.html')