# Sections Model
from django.db import models
from professor.models import ProfessorName
from courses.models import Courses

class Sections(models.Model):
  number = models.IntegerField()
  professor = models.ForeignKey(ProfessorName, on_delete=models.CASCADE)
  course = models.ForeignKey(Courses, on_delete=models.CASCADE)

  def __str__(self):
    return self.number
