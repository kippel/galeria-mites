from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
  return render_to_response('main.html');  