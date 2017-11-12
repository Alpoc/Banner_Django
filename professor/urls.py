from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.professor_list, name='professor_list'),
    url(r'^professor/view/$', views.professor_list, name='professor_list'),
    url(r'^professor/new/$', views.professor_new, name='professor_new'),
]
