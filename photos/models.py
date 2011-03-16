from django.db import models
import uuid


def get_file_path(instance, filename):
  ext = filename.split('.')[-1]
  filename = "%s.%s" % (uuid.uuid4(), ext)
  return os.path.join('photos', filename)



# Create your models here.
class Photos(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  photo = models.ImageField(upload_to=get_file_path)
  tags = models.TextField()
  
  
  
  ## posar com a fulltext els tags