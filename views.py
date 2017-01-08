from django.shortcuts import render_to_response, get_object_or_404
from varkey.blog.models import Blog, Comments

def index(request):
	return render_to_response('index.html',{
			'posts' : Blog.objects.all()[:3]
		})

def post(request, slug):
	return render_to_response('post.html', {
			'post' : get_object_or_404(Blog, slug=slug)
		})
	
