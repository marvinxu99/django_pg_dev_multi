from django import forms
from django.utils.translation import ugettext_lazy as _


from ..models import Issue, Comment, Project


TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)


class IssueCreateForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'id':'id_description_edit'}), 
        max_length=4000,
        required=False,
        help_text='The max length of the text is 4000.'
    )
    project = forms.ModelChoiceField(queryset=Project.objects, empty_label=None)

    class Meta:
        model = Issue
        fields = ('project', 'issue_type', 'title', 'priority', 'description', 'tags', )

    def clean_description(self):
        '''Ensure field is not empty'''
        desc = self.cleaned_data.get('description')
        if not desc:
            raise forms.ValidationError(_('This field should not be empty.'), code='invalid')
        return desc


class IssueEditForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'id':'id_description_edit'}), 
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Issue
        fields = ('title', 'issue_type', 'priority', 'is_resolved', 'resolved_date', 'resolution_details', 'description', 'tags', )
        widgets = {
            'is_resolved': forms.Select(choices=TRUE_FALSE_CHOICES, attrs={'style':'width:150px;'}),
            'resolved_date': forms.DateInput(attrs={'type': 'date', 'style':'width:200px;'}),
        }


class IssueEditDescriptionForm(forms.ModelForm):
    '''
    It is used for data validation purpose
    '''
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'id':'id_description_edit'}), 
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Issue
        fields = ('description', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
    
    def clean_comment(self):
        '''Ensure the field is not empty'''
        comment = self.cleaned_data.get('comment')
        if not comment:
            raise forms.ValidationError(_('This field should not be empty.'), code='invalid')
        return comment


class IssueEditTags(forms.ModelForm):
    '''
    Edit issue tags
    '''
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'id':'id_description_edit'}), 
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Issue
        fields = ('tags', )
