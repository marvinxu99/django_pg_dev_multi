from django import forms
from django.utils.translation import ugettext_lazy as _


from ..models import IssueToIssueLink, Issue


class IssueToIssueLinkForm(forms.ModelForm):
    def __init__(self, project_id, exclude_pks, *args,**kwargs):
        super (IssueToIssueLinkForm, self ).__init__(*args,**kwargs)
        self.fields['linked_to_issue'].queryset = Issue.objects.filter(project__pk=project_id).exclude(pk__in=exclude_pks)

    class Meta:
        model = IssueToIssueLink
        fields = ('link_from_type', 'linked_to_issue')
        labels = {
            'link_from_type': 'This issue',
            'linked_to_issue': 'the issue',
        }
