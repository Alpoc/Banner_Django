from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courses_list, name='courses_list'),
    url(r'^courses/view/$', views.courses_list, name='courses_list'),
    url(r'^courses/new/$', views.courses_new, name='courses_new'),
]
