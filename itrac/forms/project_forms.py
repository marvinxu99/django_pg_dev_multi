from django import forms
from django.utils.translation import ugettext_lazy as _


from ..models import Project


class ProjectForm(forms.ModelForm):
    code = forms.CharField(
        max_length=20,
        help_text='The max length is 20.'
    )
    title = forms.CharField(
        max_length=150,
        help_text='The max length is 150.'
    )

    class Meta:
        model = Project
        fields = ('code', 'title', )
