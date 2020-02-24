"""Post forms"""

# DJango
from django import forms

# MOdels
from posts.models import Post


class PostForm(forms.ModelForm):
    """MOdel form"""
    class Meta:
        model = Post
        fields = ('user', 'profile', 'title', 'photo')