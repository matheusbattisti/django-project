from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def post_list(request):
	post_list = Post.objects.all().order_by('-created_at')
	paginator = Paginator(post_list, 3)

	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_create(request):
	form = PostForm()

	if(request.method == 'POST'):

		form = PostForm(request.POST)

		if(form.is_valid()):
			post_title = form.cleaned_data['title']
			post_slug = form.cleaned_data['slug']
			post_body = form.cleaned_data['body']
			post_author = form.cleaned_data['author']
			post_status = form.cleaned_data['status']

			new_post = Post(title=post_title, slug=post_slug, body=post_body, author=post_author, status=post_status)
			new_post.save()

			return redirect('blog:post_list')
		else:
			return render(request, 'blog/add_post.html', {'form' : form})

	elif(request.method == 'GET'):
		return render(request, 'blog/add_post.html', {'form' : form})

@login_required
def post_update(request, id):
	post = get_object_or_404(Post, pk=id)
	form = PostForm(instance=post)

	if(request.method == 'POST'):
		form = PostForm(request.POST, instance=post)
		
		if(form.is_valid()):
			post = form.save(commit=False)
			post.title = form.cleaned_data['title']
			post.description = form.cleaned_data['slug']
			post.body = form.cleaned_data['body']
			post.author = form.cleaned_data['author']
			post.status = form.cleaned_data['status']

			post.save()

			return redirect('blog:post_list')
		else:
			return render(request, 'blog/edit_post.html', {'form': form, 'post' : post})

	elif(request.method == 'GET'):
		return render(request, 'blog/edit_post.html', {'form': form, 'post' : post})


def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
	return render(request, 'blog/contact.html')
