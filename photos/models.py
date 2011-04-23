from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib import admin
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
  
  def image_field(self):
    return "<img src='%s' width='120px' />" % self.photo.url

  image_field.short_description = 'Thumbnail'	
  image_field.allow_tags = True

class PhotosAdmin(admin.ModelAdmin):
  list_display = ('image_field', 'photo', 'tags')
  pass
  
admin.site.register(Photos, PhotosAdmin)
  