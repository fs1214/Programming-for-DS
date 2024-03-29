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
			#if 'name' in context and 'end_date' in context and 'start_date' in context:
			context['name'] = request.GET['name']
			context['start_date'] = request.GET['start_date']
			context['end_date'] = request.GET['end_date']
	
	print context
				
	requestContext = RequestContext(request, context)

	templateIndex = loader.get_template('index.html')

	renderedTemplate = templateIndex.render(requestContext)

	response = HttpResponse()

	response['Age'] = 120

	response.write(renderedTemplate)
	
	if 'name' in context:# and 'end_date' in context and 'start_date' in context:
		company = context['name'].encode('ascii','ignore')
		start_date = context['start_date'].encode('ascii','ignore')
		end_date = context['end_date'].encode('ascii','ignore')
		a = request.GET.get('name')
		start_date = start_date.split('-')
		end_date = end_date.split('-')
		
		start = datetime.datetime(int(start_date[0]),int(start_date[1]),int(start_date[2]))
		end = datetime.datetime(int(end_date[0]),int(end_date[1]),int(end_date[2]))
		
		f = web.DataReader(company,'yahoo',start,end)
		a = f['Close']
		b = a.index.tolist()
		array = []
		for i in range(b.__len__()):
			c = b[i]
			s = str(c)[:10]
			d = a.tolist()
			e = round(d[i],2)
			array.append(e)
		
		return render_to_response('index.html',{'array':json.dumps(array), 'start_date':json.dumps(start_date), 'end_date':json.dumps(end_date)})
	return render_to_response('index.html',{})
