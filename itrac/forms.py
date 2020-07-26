from django import forms
from .models import Issue, Comment, Reply


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'issue_type', 'description', 'image', 'tags', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply',)