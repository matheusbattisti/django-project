from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
	post_list = Post.objects.all().order_by('-created_at')
	paginator = Paginator(post_list, 3)

	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_detail.html', {'post':post})

def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
	return render(request, 'blog/contact.html')
