from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=200)
  path_to_folder = models.CharField(max_length=200)
  date_created = models.DateTimeField('date created')

  def __str__(self):
    return self.title

class Part(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  priority = models.IntegerField(default=10)
  status = models.CharField(max_length=20, default='Не активен')
  date_created = models.DateTimeField('date created')

  def __str__(self):
    return self.title

class Programm(models.Model):
  part = models.ForeignKey(Part, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  type = models.CharField(max_length=100)
  path_to_folder = models.CharField(max_length=300)
  date_created = models.DateTimeField('date created')

  def __str__(self):
    return self.title