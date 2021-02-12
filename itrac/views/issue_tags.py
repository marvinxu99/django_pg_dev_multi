from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json

from ..models import Issue, Tag


@login_required
def edit_issue_tags(request, pk):
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    tags_to_exclude = [tag.title for tag in issue.tags.all()]
    tags = Tag.objects.exclude(title__in=tags_to_exclude)
    data['html_tags_edit_list'] = render_to_string(
        'includes/partial_issue_details_tags/partial_issue_details_tags_edit.html',
        { 'issue': issue, 'tags': tags }
    )
    return JsonResponse(data)


@login_required
def partial_issue_tags_list(request, pk):
    '''Return all existing tags (each surfixed with a remove button)
    '''
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    data['html_issue_tags_list'] = render_to_string(
        'includes/partial_issue_details_tags/partial_issue_details_tags_list.html',
        { 'issue': issue }
    )
    return JsonResponse(data)

@login_required
def issue_delete_tag(request, pk, tag_pk):
    ''' Remove the tag from the issue's tags set
    '''
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    tag = get_object_or_404(Tag, pk=tag_pk)
    issue.tags.remove(tag)
    data['status'] = 'S'
    return JsonResponse(data)

@login_required
def issue_add_tag(request, pk, tag_pk):
    ''' Add a tag to the issue (the tag already exists in the Tag table)
    '''
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    tag = get_object_or_404(Tag, pk=tag_pk)
    issue.tags.add(tag)
    data['status'] = 'S'
    return JsonResponse(data)


@login_required
@require_POST
def issue_add_net_new_tag(request, pk):
    ''' Add a net new tag to the issue and to the Tag table
    '''
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)

    tag_data = json.loads(request.body)
    tag, _ = Tag.objects.get_or_create(
        title=tag_data['new_tag'],
        created_by=request.user,
        updated_by=request.user,
    )

    issue.tags.add(tag)
    data['status'] = 'S'

    return JsonResponse(data)
