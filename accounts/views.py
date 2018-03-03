from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def login_success(request):
    if request.user.is_prof==True:
        return redirect('accounts/moodle_prof')
    elif request.user.is_admin==True:
        return redirect('admin/')
    else:
        return redirect('accounts/moodle_stud')

def index(request):
    return render(request,'index.html')