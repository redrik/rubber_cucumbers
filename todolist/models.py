from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=200)
  path_to_folder = models.CharField(max_length=200)
  date_created = models.DateTimeField('date created')

class Detail(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  priority = models.IntegerField(max_length=10, default=0)
  date_created = models.DateTimeField('date created')

class Programm(models.Model):
  detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  type = models.CharField(max_length=100)
  path_to_folder = models.CharField(max_length=300)
  date_created = models.DateTimeField('date created')