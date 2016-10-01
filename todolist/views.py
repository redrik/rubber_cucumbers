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
  project = Project.objects.get(pk=project_id)
  return render(request, 'todolist/part.html', {'part_list': part_list, 'project': project})

def programm_of_part(request, part_id):
  programm_list = Programm.objects.filter(part=part_id)
  part = Part.objects.get(pk=part_id)
  project = Project.objects.get(pk=part.project.id)
  return render(request, 'todolist/programm.html', {'programm_list': programm_list, 'part': part, 'project': project}) 