from django.shortcuts import render
from moodle_prof.models import course,course1,message

# Create your views here.
def index(request):
    all_courses = course1.objects.all().filter(user=request.user)
    all_messages=message.objects.all().filter(user=request.user)
    all_courses_all=course.objects.all()
    context={
        'all_courses':all_courses,
        'all_messages':all_messages,
        'all_courses_all':all_courses_all
    }
    return render(request,'moodle_stud_index.html', context)

def course_add(request):
    if request.method=="POST":
        courset=course1.objects.all().get(course_code=request.POST.get('code'))
        courset.user.add(request.user)
    return render(request,'course_add_stud.html')

def course_drop(request):
    if request.method == "POST":
        code=request.POST.get('code')
        courset=course1.objects.all().get(course_code=code)
        courset.user.remove(request.user)

        for messages in message.objects.all().filter(course__course_code=code).filter(user=request.user):
            messages.user.remove(request.user)
    return render(request,'course_drop_stud.html')