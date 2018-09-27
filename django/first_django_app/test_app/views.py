from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
	print('hello from the index route')
	return HttpResponse('This is kind of like a res.send in express')

def bob(request):
	print('Bob says hi')
	bobs_books = Book.objects.all().order_by('title')
	return render(request,
		'test_app/bob.html', 
		{ 

			'bobs_fave_food': 'Beans', 
			'bob_is_tired': True,
			'bobs_pets': ['dog', 'dog', 'cat', 'bird'],
			'bobs_books': bobs_books
		})