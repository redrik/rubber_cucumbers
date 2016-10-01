from django.conf.urls import url

from . import views

app_name = 'todolist'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<project_id>[0-9]+)/$', views.part_of_project, name='part_of_project'),
  ]