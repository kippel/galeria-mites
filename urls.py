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
