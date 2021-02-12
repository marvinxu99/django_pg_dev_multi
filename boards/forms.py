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

    # NOT NEEDED. left here as an example showing how to clean data
    # def clean_message(self):
    #     message = self.cleaned_data.get('message')
    #     if not message:
    #         # do some validation, if it fails
    #         raise forms.ValidationError(u'Form error')
    #     return message


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
