from django.shortcuts import render
from .models import Album
from django.template import loader
from django.http import Http404
# Create your views here.

from django.http import HttpResponse

def index(request):
	albums = Album.objects.all()
	""" sending html without template
	html = ''
	for album in albums:
		url = '/music/'+str(album.id)+'/'
		html += '<a href="'+url+'">'+album.album_title+'</a><br>'
	"""
	context={"albums" : albums}
	""" sending template using loader
	template = loader.get_template("music/index.html")
	return HttpResponse(template.render(context,request))
	"""
	return render(request,"music/index.html",context)

def details(request,album_id):
	try:
		album = Album.objects.get(id=album_id)
	except Album.DoesNotExist:
		raise Http404("this is the mesasage for 404 error")
	return render(request,"music/detail.html",{"album":album})