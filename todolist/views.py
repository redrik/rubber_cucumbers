from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import F

from .models import Project, Part, Programm


class IndexView(generic.ListView):
  template_name = 'todolist/index.html'
  context_object_name = 'project_list'

  def get_queryset(self):
    return Project.objects.order_by('-date_created')[:5]

class PartView(generic.ListView):
  context_object_name = 'part_list'
  template_name = 'todolist/parts.html'

  def get_queryset(self):

    return Part.objects.filter(project_id=1)