# posts/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        # widget=forms.Textarea(),
        widget=forms.TextInput(
            attrs={'placeholder': "Your post title", "size": 40}
        ),
        max_length=140,
        help_text='The max length of the title is 140.'
    )

    class Meta:
        model = Post
        fields = ['title', 'cover']

    def clean_image(self):
        image = self.cleaned_data.get['image']
        if image:
            # do some validation, if it fails
            raise forms.ValidationError(u'Form error')
        return image
