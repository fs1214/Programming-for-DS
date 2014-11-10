from django.shortcuts import render_to_response
from matplotlib import pylab
from pylab import * 
from blog.models import posts
import json
import PIL
import PIL.Image
import StringIO
from django.http import HttpResponse
from django.template import RequestContext, loader
import pythoncode
import pandas.io.data as web
import datetime
 
def home(request):
    a = request.GET.get('name')    
    start = datetime.datetime(2010,1,1)
    end = datetime.datetime(2010,1,15)
    f = web.DataReader('IBM','yahoo',start,end)
    a = f['Open']
    b = a.index.tolist()
    array = [['date', 'price']]
    for i in range(b.__len__()):
	c = b[i]
    	s = str(c)[:10]
    	d = a.tolist()
    	e = round(d[i],2)    
    	array.append([s,e])
	print "abc"
	
    	
    return render_to_response('index.html',{'array':json.dumps(array)})





	# Create your views here.
