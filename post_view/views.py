from django.shortcuts import render
from .models import Post
# Create your views here.


def PostListView(request):
    posts = Post.objects.all().order_by('-published_at')
    context = {
        'posts': posts
    }
    return render(request, 'post_view/post_list.html', context)