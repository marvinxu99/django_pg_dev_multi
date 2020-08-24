from django import forms
from django.utils.translation import ugettext_lazy as _


from ..models import Project


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        max_length=150,
        help_text='The max length is 150.'
    )
    code = forms.CharField(
        max_length=20,
        help_text='The max length is 20.'
    )

    class Meta:
        model = Project
        fields = ('title', 'code',)
