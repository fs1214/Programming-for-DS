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
	context = {}
	context['requestMethod'] = request.META['REQUEST_METHOD']

	if request.method == 'GET' :

		if request.GET.__contains__('hidden') :

		  context['name'] = request.GET['name']

	requestContext = RequestContext(request, context)

	templateIndex = loader.get_template('index.html')

	renderedTemplate = templateIndex.render(requestContext)

	response = HttpResponse()

	response['Age'] = 120

	response.write(renderedTemplate)
	
	if 'name' in context:
		company = context['name'].encode('ascii','ignore')
		a = request.GET.get('name')
		start = datetime.datetime(2013,12,1)
		end = datetime.datetime(2013,12,15)
		f = web.DataReader(company,'yahoo',start,end)
		a = f['Open']
		b = a.index.tolist()
		array = [['date', 'price']]
		for i in range(b.__len__()):
			c = b[i]
			s = str(c)[:10]
			d = a.tolist()
			e = round(d[i],2)
			array.append([s,e])
		
		return render_to_response('index.html',{'array':json.dumps(array)})
	return render_to_response('index.html',{})

