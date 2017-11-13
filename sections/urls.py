# Sections urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sections_list, name='sections_list'),
    url(r'^sections/view/$', views.sections_list, name='sections_list'),
    url(r'^sections/new/$', views.sections_new, name='sections_new'),
]
