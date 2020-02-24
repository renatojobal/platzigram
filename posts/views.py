"""Posts views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Form
from posts.forms import PostForm

# Models
from posts.models import Post


@login_required
def list_posts(request):
    # Traemos todos los post
    queryset = Post.objects.all().order_by('-created')

    return render(request=request,
        template_name='posts/feed.html',
        context={
            'posts': queryset
            }
    )


@login_required
def create_post(request):
    """Create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()


    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )