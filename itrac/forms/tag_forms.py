from django import forms
from django.utils.translation import ugettext_lazy as _


from ..models import Tag


class TagCreateForm(forms.ModelForm):
    title = forms.CharField(
        max_length=40,
        help_text='The max length is 40.'
    )

    class Meta:
        model = Tag
        fields = ('title',)

DISPLAY_CHOICES = (
    ("locationbox", "Display Location"),
    ("displaybox", "Display Direction")
)

class TagEditForm(forms.ModelForm):
    title = forms.CharField(
        max_length=40,
        help_text='The max length is 40.'
    )
    is_active = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'choice-no-bullets'}), 
        choices=[
            (True, 'Yes'),
            (False, 'No'),
        ]
    )

    class Meta:
        model = Tag
        fields = ('title','is_active')
        # widgets = {'is_active': forms.RadioSelect(choices=[
        #     (True, 'Yes'),
        #     (False, 'No'),        
        # ])}
