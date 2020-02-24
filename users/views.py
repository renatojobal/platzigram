#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

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

            return redirect('update_profile')
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
            return redirect('feed')
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
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if(password != password_confirmation):
            return render(request, 'users/signup.html', {'error': 'Passwords does not match'})



        if(User.objects.filter(username=username).exists()):
            return render(request, 'users/signup.html', {'error': 'This username is already taken'})

        user = User.objects.create_user(username=username, 
                        password=password, 
                        first_name=first_name,
                        last_name=last_name,
                        email=email)

        profile = Profile(user=user)
        profile.save()
        return redirect('logout')


    return render(request, 'users/signup.html')