from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^course_add/$', views.course_add, name='course_add'),
    url(r'^course_drop/$', views.course_drop, name='course_add'),
    url(r'^message_add/$', views.message_add, name='message_add'),
]