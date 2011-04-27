# -*- coding: utf-8 -*-
#
#       models.py     
#       
#       Copyright 2011 David <kippeld@gmail.com>            
#                      Arnau <sacaix@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
# 
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()

# Create your models here.
class Photos(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nom:')
  description = models.TextField(blank=True, null=True, verbose_name=u'Descripció:')
  photo = models.ImageField(storage=fs, upload_to='photos', verbose_name='Fotografia*:')
  tags = models.CharField(max_length=200, verbose_name='Tags*:')
  
  def image_field(self):
    return "<img src='%s' width='120px' />" % self.photo.url

  image_field.short_description = 'Thumbnail'	
  image_field.allow_tags = True

