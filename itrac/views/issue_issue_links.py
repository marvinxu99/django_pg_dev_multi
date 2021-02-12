from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
import json

from ..models import Issue, ISSUE_LINK_TYPE, IssueToIssueLink
from ..forms import IssueToIssueLinkForm


@login_required
def issue_links_add_issue(request, pk):
    data = dict()
    exclude_pks = []

    current_project = request.session.get('current_project', { 'project': 'WINN', 'id': 0 })

    issue = get_object_or_404(Issue, pk=pk)

    # Exclude itself and already linked issues
    exclude_pks.append(issue.pk)
    for linked in issue.linked_to_issues.all():
        exclude_pks.append(linked.linked_to_issue.pk)
    for linked in issue.linked_from_issues.all():
        exclude_pks.append(linked.linked_from_issue.pk)

    if request.method == 'POST':
        form = IssueToIssueLinkForm(current_project['id'], exclude_pks, request.POST)
        if form.is_valid():
            issue_to_issue_link = form.save(commit=False)
            issue_to_issue_link.linked_from_issue = issue
            issue_to_issue_link.updated_date = timezone.now()
            issue_to_issue_link.updated_by = request.user
            issue_to_issue_link.save()

            data['form_is_valid'] = True
            data['html_links_list'] = render_to_string(
                'includes/partial_issue_details_links/partial_issue_details_links_list.html',
                { 'issue': issue }
            )
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
    else:
        form = IssueToIssueLinkForm(current_project['id'], exclude_pks)

    context = {
        'form': form,
        'issue': issue,
    }
    data['html_form'] = render_to_string(
        'includes/partial_issue_details_links/partial_issue_details_links_add_link_form.html',
        context,
        request=request
    )

    return JsonResponse(data)



@login_required
def issue_links_delete_issue(request, pk, linked_pk):
    '''Delete an issue link
    '''
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)

    try:
        issue_issue_link = IssueToIssueLink.objects.filter(linked_from_issue_id=pk, linked_to_issue_id=linked_pk)
        issue_issue_link[0].delete()
    except:
        pass

    data['status'] = 'S'
    data['html_links_list'] = render_to_string(
        'includes/partial_issue_details_links/partial_issue_details_links_list.html',
        { 'issue': issue }
    )
    return JsonResponse(data)
