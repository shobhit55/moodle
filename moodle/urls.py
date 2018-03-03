"""moodle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include,url
from accounts import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/$',auth_views.login,name='login'),
    url(r'logout/$',auth_views.logout,name='logout'),
    url(r'accounts/moodle_prof/', include('moodle_prof.urls')),
    url(r'accounts/moodle_stud/', include('moodle_stud.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login_success$',views.login_success,name='login_success'),
]