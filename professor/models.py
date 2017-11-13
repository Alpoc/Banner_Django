# Professor Model
from django.db import models
from django.utils import timezone


class ProfessorName(models.Model):
  author = models.ForeignKey('auth.User')
  name = models.CharField(max_length=200)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

