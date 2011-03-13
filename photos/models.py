from django.db import models

# Create your models here.
class Photos(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  file_name = models.CharField(max_length=100)
  tags = models.TextField()
  ## posar com a fulltext els tags