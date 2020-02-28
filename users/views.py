#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
from users.models import Profile
from django.views.generic import TemplateView, DetailView

# MOdels
from django.contrib.auth.models import User

# Forms
from users.forms import (ProfileForm,
                        SignupForm)



class UserDetailView(DetailView):
    """User detail view"""

    temaplete_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()





@login_required
def update_profile(request):
    """Update user's profile view"""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.picture = data['picture']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']

            profile.save()

            return redirect('users:update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )




# Create your views here.
def login_view(request):
    """Login view"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', context={'error': 'Invalid username or password'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout view"""

    logout(request)
    return redirect('login')


def signup(request):
    """Signup view"""

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm



    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form})