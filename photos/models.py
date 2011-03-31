from django.db import models
from django.core.files.storage import FileSystemStorage
import uuid

"""
def get_file_path(instance, filename):
  ext = filename.split('.')[-1]
  filename = "%s.%s" % (uuid.uuid4(), ext)
  return os.path.join('photos', filename)
"""
fs = FileSystemStorage()

# Create your models here.
class Photos(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  photo = models.ImageField(storage=fs, upload_to='photos')
  tags = models.CharField(max_length=200)
  
  
  
  ## posar com a fulltext els tags