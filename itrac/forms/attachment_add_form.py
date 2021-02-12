# posts/forms.py
from django import forms
from ..models import IssueAttachment

class AttachmentAddForm(forms.ModelForm):
    # description = forms.CharField(
    #     # widget=forms.Textarea(),
    #     widget=forms.TextInput(
    #         attrs={'placeholder': "description", "size": 40}
    #     ),
    #     max_length = 40,
    #     # help_text='The max length of description is 100.'
    # )

    class Meta:
        model = IssueAttachment
        # fields = ['attachment', 'description', ]
        fields = ['attachment', ]
