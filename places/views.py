from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Place


def index(request):
	places_list = Place.objects.all()
#	output = ', '.join([p.name for p in places_list])
	output = serializers.serialize("json",  places_list, fields = ('name'))
	return HttpResponse(output)

def cafes(request):
	return HttpResponse("Index of Cafes.")
# Create your views here.
