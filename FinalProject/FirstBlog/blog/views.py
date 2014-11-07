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
    content = {
		'title' : 'My First Post',
		'author' : 'lzr',
		'date' : '11/07/14',
		'body' : 'wqnmlgb',
	}
    if(request.POST.get('mybtn')):
        print('click')		
    return render_to_response('index.html',content)

def request_page(request):
	if(request.POST.get('mybtn')):
		print('click')
	return render_to_response('index.html')

def graph(request):
	x = [1,2,3,4,5,6]
	y = [5,2,6,8,2,7]
	plot(x,y, linewidth=2)

	buffer = StringIO.StringIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	graphIMG = PIL.Image.fromstring("RGB",canvas.get_width_height(), canvas.tostring_rgb())
	graphIMG.save(buffer,"PNG")
	pylab.close()

	return HttpResponse(buffer.getvalue(), mimetype="image/png")






	# Create your views here.
