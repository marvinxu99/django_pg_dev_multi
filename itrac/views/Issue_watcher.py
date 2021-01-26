from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
import json

from ..models import Issue, IssueWatcher


@login_required
@require_POST
def issue_start_watch(request, pk):
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)

    data['status'] = 'S'
    data['html_list'] = render_to_string(
        'includes/partial_issue_watcher_button/partial_issue_watcher_button_stop.html',
        { 'issue': issue }
    )
    return JsonResponse(data)


@login_required
def issue_stop_watching(request, pk):
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)

    data['status'] = 'S'
    data['html_list'] = render_to_string(
        'includes/partial_issue_watcher_button/partial_issue_watcher_button_start.html',
        { 'issue': issue }
    )
    return JsonResponse(data)


@login_required
def issue_add_watcher(request, pk, user_id):
    '''Delete an attachment
    '''
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)

    try:
        attachment = IssueAttachment.objects.filter(issue=issue, pk=att_pk)
        attachment[0].delete()
        
    except:
        pass
    
    data['status'] = 'S'
    data['html_list'] = render_to_string(
        'includes/partial_issue_details_attachments/partial_issue_details_attachments_list.html',
        { 
            'issue': issue,
            'user': request.user 
        },
        
    )
    return JsonResponse(data)