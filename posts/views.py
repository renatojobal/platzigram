"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'


@login_required
def create_post(request):
    """Create new post view."""

    if request.method == 'POST':
        # Si el método http es POST, entra aquí y guarda un nuevo 'posst'
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Lo manda a la url dedl feed
            return redirect('posts:feed')

    else:
        form = PostForm()

    # Si llega acá, significa que no es método http POST,
    # entonces se entiende que el cliente solo quiere el formulario
    # para crear el post
    return render(
        request=request,
         # Entonces lo manda al template para crear el post:
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
