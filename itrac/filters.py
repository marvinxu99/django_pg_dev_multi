from .models import Issue
import django_filters

class IssueFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Issue
        fields = ['issue_type', 'title', 'status', 'priority', 'is_resolved', 'tags', 'author', 'assignee']


# Super ursers can view all projects
class IssueFilter_superuser(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Issue
        fields = ['project', 'issue_type', 'title', 'status', 'priority', 'is_resolved', 'tags', 'author', 'assignee']