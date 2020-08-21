from .models import Issue
import django_filters

class IssueFilter(django_filters.FilterSet):
    class Meta:
        model = Issue
        fields = ['project', 'issue_type', 'status', 'is_resolved', 'tags', 'author', 'assignee']