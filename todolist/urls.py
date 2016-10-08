from django.conf.urls import url

from . import views

app_name = 'todolist'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<project_id>[0-9]+)/$', views.part_of_project, name='part_of_project'),
  url(r'^part/(?P<part_id>[0-9]+)/$', views.programm_of_part, name='programm_of_part'),
  ]