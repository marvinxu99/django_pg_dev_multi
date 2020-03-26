from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        # widget=forms.Textarea(), 
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': "What is on your mind?"}
        ), 
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


# Used in reply_topic() 
class PostForm(forms.ModelForm):
    message = forms.CharField(
        # widget=forms.Textarea(), 
        widget=forms.Textarea(
            attrs={'rows': 5}
        ), 
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Post
        fields = ['message', ]