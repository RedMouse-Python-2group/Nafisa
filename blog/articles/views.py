from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from forms import CommentForm

# Create your views here.

def home_page(requests):
	articles = Post.objects.all()
	context = {'articles_list': articles}
	return render (requests, 'pages/home.html', context)

def post_detail(requests, id = None):
	post = get_object_or_404 (Post, id = id)
	form = CommentForm(requests.POST or None)
	if form.is_valid():
		comment = form.save(commit = False)
		comment.post = post
		comment.save()
		return redirect (requests.path)

	context = {'post': post,
                'form':form
	          }
	return render (requests, 'pages/post_read.html', context)


def about_page(requests):
	return render (requests, "pages/about.html")
