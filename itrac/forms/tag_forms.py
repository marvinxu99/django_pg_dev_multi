from django import forms
from django.utils.html import mark_safe

from ..models import Tag


class TagCreateForm(forms.ModelForm):
    title = forms.CharField(
        max_length=40,
        help_text='The max length is 40.'
    )

    class Meta:
        model = Tag
        fields = ('title',)


class TagEditForm(forms.ModelForm):
    title = forms.CharField(
        max_length=40,
        help_text='(maximum length is 40)'
    )
    is_active = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={ 'class': 'choice-no-bullets' }),
        choices=[
            (True, 'Yes'),
            (False, 'No'),
        ]
    )

    class Meta:
        model = Tag
        fields = ('title','is_active')
