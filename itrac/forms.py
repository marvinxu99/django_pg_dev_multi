from django import forms
from .models import Issue, Comment, Reply


TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'issue_type', 'is_resolved', 'resolved_date', 'description', 'image', 'tags', )
        widgets = {
            'is_resolved': forms.Select(choices=TRUE_FALSE_CHOICES, attrs={'style':'width:120px;'}),
            'resolved_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply',)