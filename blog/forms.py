from django import forms

from .models import Post, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('title', 'photo')