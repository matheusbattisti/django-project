from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
	return render(request, 'blog/post_list.html')

def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
	return render(request, 'blog/contact.html')
