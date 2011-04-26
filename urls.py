# -*- coding: utf-8 -*-
#
#       urls.py     
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
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', 'photos.views.index'),
    (r'^load/?$', 'photos.views.load'),
    (r'^upload/?$', 'photos.views.upload'),
    # (r'^gll/', include('gll.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^static_media/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': '/home/kippel/src/gll/media'}),
     
     (r'^admin/', include(admin.site.urls)),
)
