# posts/forms.py
from django import forms
from ..models import IssueAttachment

class AttachmentAddForm(forms.ModelForm):
    title = forms.CharField(
        # widget=forms.Textarea(), 
        widget=forms.TextInput(
            attrs={'placeholder': "description", "size": 100}
        ), 
        max_length=255,
        help_text='The max length of description is 255.'
    )

    class Meta:
        model = IssueAttachment
        fields = ['description', 'attachment']

