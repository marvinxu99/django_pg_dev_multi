from django import forms
from django.utils.translation import ugettext_lazy as _


from ..models import Project


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        max_length=150,
        help_text='The max length is 100.'
    )
    code = forms.CharField(
        max_length=20,
        help_text='The max length is 20.'
    )

    description = forms.CharField(
        max_length=250,
        help_text='The max length is 250.'
    )

    category = forms.CharField(
        max_length=40,
        required=False,
        help_text='The max length is 40.'
    )
    URL = forms.CharField(
        max_length=250,
        required=False,
        help_text='The max length is 250.'
    )

    class Meta:
        model = Project
        fields = ('title', 'code', 'description', 'category', 'URL')
