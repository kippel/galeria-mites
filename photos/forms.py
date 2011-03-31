from photos.models import Photos
from django.forms import ModelForm

class PhotosForm(ModelForm):
  class Meta:
    model = Photos