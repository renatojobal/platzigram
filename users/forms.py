"""
User forms
"""



# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Signup Form"""

    username = forms.CharField(min_length=4, 
                            max_length=50, 
                            required=True)
    password = forms.CharField(min_length=8,
                                max_length=70,
                                widget=forms.PasswordInput(),
                                required=True)
    password_confirmation = forms.CharField(min_length=8,
                                max_length=70,
                                widget=forms.PasswordInput(),
                                required=True)

    first_name = forms.CharField(min_length=2, max_length=50)
    lastt_name = forms.CharField(min_length=2, max_length=50)

    email = forms.EmailField(min_length=6, 
                            max_length=70)

    # Validando un cmapo en especifico

    def clean__username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        query = User.objects.filter(username=username).exist()
        if query:
            raise forms.ValidationError('Username is already in use')
        
        # ! Siempre regresar el campo luego ded regresarlo
        return username


    # Validando campos dependientes, lo hacemos en el último
    # método que se llama que es 'clean()'
    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return data
        
    def save(self):
        """Create an user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)

        profile = Profile(user=user)
        profile.save()



class ProfileForm(forms.Form):
    """Profile form"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=False)

