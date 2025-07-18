from django import forms
from .models import Post
from django.core.validators import MinLengthValidator

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter an eye-catching title...'
        })
    )
    content = forms.CharField(
        validators=[MinLengthValidator(50, message="Your post must be at least 50 characters long")],
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 10,
            'placeholder': 'Share your thoughts here...'
        })
    )
    author = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name'
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
        })
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']
