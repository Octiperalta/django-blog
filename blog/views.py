from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import CommentForm
# Create your views here.


def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})


def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    comments = post.comments.filter()

    user_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            print('DEBUGG')

            comment_form = CommentForm()
            return render(request, "post_details.html", {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form})
            # return HttpResponseRedirect('')
    else:
        comment_form = CommentForm()

    return render(request, 'post_details.html', {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form})
    # return render(request, 'post_details.html', {'post': post})
