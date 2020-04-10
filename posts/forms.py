# posts/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        # widget=forms.Textarea(), 
        widget=forms.TextInput(
            attrs={'placeholder': "enter a title "}
        ), 
        max_length=140,
        help_text='The max length of the title is 140.'
    )

    class Meta:
        model = Post
        fields = ['title', 'cover']