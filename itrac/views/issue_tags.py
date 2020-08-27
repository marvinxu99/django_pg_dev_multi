from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from ..models import Issue


@login_required
def edit_issue_tags(request, pk):
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    data['html_tags_edit_list'] = render_to_string('includes/partial_issue_tags_edit.html', 
        { 'issue': issue }
    )
    return JsonResponse(data)


@login_required
def partial_issue_tags_list(request, pk):
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    data['html_issue_tags_list'] = render_to_string('includes/partial_issue_tags_list.html', 
        { 'issue': issue }
    )
    return JsonResponse(data)
    

