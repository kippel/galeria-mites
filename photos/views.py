from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from photos.models import Photos
from django.utils import simplejson
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt

def index(request):
  return render_to_response('main.html')
 
@csrf_exempt 
def load(request):
  
  result = {'html':'', 'error':False, 'num':0}
    
  if request.method == 'POST':
    search = request.POST.get('search','')
    
    search = search.replace(',',' ')
    
    photos = Photos.objects.filter(tags__search=search)
  
    if len(photos) >0:
      result['html'] = loader.get_template('galeria.html').render(Context({'photos':photos}))
  
    result['num'] = len(photos)
        
  return HttpResponse(simplejson.dumps(result) , mimetype='application/json')
    