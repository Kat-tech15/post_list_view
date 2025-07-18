from django.shortcuts import render, redirect
from .models import Post
from .forms import BlogForm

# Create your views here.

def create_blog(request):
    success = False
    post = None
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            success = True
            form = BlogForm()  # Reset the form after successful submission
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {
        'form': form, 
        'success': success,
        'post': post
    })
