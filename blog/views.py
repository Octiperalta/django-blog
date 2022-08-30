from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})


def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'post_details.html', {'post': post})
