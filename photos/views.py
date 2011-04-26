from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from photos.models import Photos
from photos.forms import PhotosForm
from django.utils import simplejson
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import math

def gen_tag_from_photos(photos, threshold=0, maxsize = 2.5, minsize = 1):
  taglist = {}
  # agafo els tags i els conto
  for photo in photos:
    for tag in photo.tags.rsplit(' '):
      taglist[tag] = 1+taglist.get(tag,0);

  
  # miro el maxim i el minim i elimino els que no superen el trheshold
  mincount, maxcount = 5000, 0;
  for (x, p) in taglist.items():
    if p <= threshold:
      del taglist[x]
      continue
    
    if p > maxcount:
      maxcount=p
    if p < mincount:
      mincount=p
  
  constant = (math.log(maxcount -(mincount -1 )) /(maxsize -minsize or 1)  or 1)

  tagcloud = []
  for (x, p) in taglist.items():
     size = math.log(p - (mincount - 1))/constant + minsize
     tagcloud.append({
        'tag':x,
        'size': "%.2f" % size
     })
  
  return tagcloud  
  

def index(request):
  
  tags = Photos.objects.all()
  
  tagcloud= gen_tag_from_photos(tags)

  return render_to_response('main.html', {'tagcloud':tagcloud})
 
@csrf_exempt 
def load(request):
  
  result = {'html':'', 'error':False, 'num':0}
    
  if request.method == 'POST':
    search = request.POST.get('search','')
    
    search = search.replace(',',' ').lower()
    
    photos = Photos.objects.filter(tags__search=search).order_by('?')[:10]
  
    
  
    if len(photos) >0:
      result['html'] = loader.get_template('galeria.html').render(Context({'photos':photos,'tagcloud':gen_tag_from_photos(photos)}))
  
    result['num'] = len(photos)
        
  return HttpResponse(simplejson.dumps(result) , mimetype='application/json')

#@login_required
def upload(request):
  if request.method=='POST':
    form = PhotosForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    
      form = PhotosForm()
    #3else:
    #  print form.errors
      
  else:
    form = PhotosForm()
    
  return render_to_response('upload.html', {'form':form}, context_instance = RequestContext(request))    
