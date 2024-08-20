from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    """
    Form class for site owner to post their blog
    """
    class Meta:
        model = Post
        fields = '__all__'