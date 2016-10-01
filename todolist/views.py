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

def part_of_project(request, project_id):
  part_list = Part.objects.filter(project=project_id)
  return render(request, 'todolist/part.html', {'part_list': part_list})

def programm_of_part(request, part_id):
  programm_list = Programm.objects.filter(part=part_id)
  return render(request, 'todolist/programm.html', {'programm_list': programm_list})