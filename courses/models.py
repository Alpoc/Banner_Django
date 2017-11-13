# Courses Model
from django.db import models

class Courses(models.Model):
  number = models.IntegerField()
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

