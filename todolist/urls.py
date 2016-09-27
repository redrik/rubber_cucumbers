from django.conf.urls import url

from . import views

app_name = 'todolist'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>[0-9]+)/$/details', views.PartView.as_view(), name='part'),
]