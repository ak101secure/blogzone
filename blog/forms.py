# blog/forms.py
from django import forms
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'tags']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 3,
        'placeholder': 'Add a comment...'
    }))

    class Meta:
        model = Comment
        fields = ['content']