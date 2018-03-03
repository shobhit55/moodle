from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^course_add/$', views.course_add, name='course_add'),
    url(r'^course_drop/$', views.course_drop, name='course_drop'),
]