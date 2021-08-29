from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
  name = models.CharField(max_length=256)
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(max_length=256)

  def __str__(self):
    return self.name[:50]

  def get_absolute_url(self):
    return reverse('snack_detail', args=[str(self.id)])