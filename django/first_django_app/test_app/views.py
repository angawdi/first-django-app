from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	print('hello from the index route')
	return HttpResponse('This is kind of like a res.send in express')