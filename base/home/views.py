from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
# Create your views here.

def index(request):
	print(dir(request.GET))
	template = loader.get_template('home/index.html');
	return HttpResponse( template.render({}, request));

def rest(request):
	user = ['username', 1, 1.1, {'username': 'john', 'password': 'pass@123'}]
	return JsonResponse(user, safe=False);

def download(request):
	rf = open('/tmp/files/web/base/home/templates/home/index.html', 'r')
	response = HttpResponse(rf.read(), content_type="text/html");
	response['Content-Disposition'] = 'inline; filename=out.txt'
	return response;
