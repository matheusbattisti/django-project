from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
	posts = Post.objects.all().order_by('-created_at')
	return render(request, 'blog/post_list.html', {'posts':posts})

def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
	return render(request, 'blog/contact.html')
