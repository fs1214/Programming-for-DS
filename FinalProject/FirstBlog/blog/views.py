from django.shortcuts import render_to_response
from matplotlib import pylab
from pylab import * 
from blog.models import posts

import PIL
import PIL.Image
import StringIO
from django.http import HttpResponse
from django.template import RequestContext, loader
import pythoncode
 
def home(request):
    return render_to_response('index.html')





	# Create your views here.
