import os
import requests
from datetime import datetime, timedelta, time
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count, Q
from django.core import serializers
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import get_user_model
import json

from itrac.models import Issue, Comment, SavedIssue, Tag, ISSUE_STATUS, \
    IssueAttachment, IssueToIssueLink, ISSUE_LINK_TYPE
from itrac.forms import IssueEditForm, IssueCreateForm, CommentForm, IssueEditDescriptionForm
from core.constants import ACTIVE_STATUS


@login_required
def my_in_progress_issues(request):
    """
    Create a view that will return a list
    of Issues assigned to the current user.
    """
    issue_count_total = Issue.objects.count()

    if not request.session.get('current_project', False):
            request.session['current_project'] = { 'title': 'WINN', 'id': 1 }

    current_project = request.session.get('current_project', { 'title': 'WINN', 'id': 1 })

    issues = Issue.objects.filter(
            assignee=request.user,
            project__pk=current_project['id'],
            status__in = (ISSUE_STATUS.OPEN,
                            ISSUE_STATUS.INVESTIGATE,
                            ISSUE_STATUS.TRIAGE,
                            ISSUE_STATUS.BUILD_IN_PROGRESS)
        ).order_by('-created_date')

    issue_count_filter = issues.count()

    context = {
            'issue_count_total': issue_count_total,
            'issue_count_filter': issue_count_filter,
            'issues': issues,
            'filter_name': "My in Progress Issues",
            'refresh_url': reverse('itrac:my_in_progress_issues'),
        }

    return render(request, "itrac/issues.html", context)


@login_required()
def issues_reported_by_me(request):
    """
    Create a view that will return a list
    of current user's Issues and render them to the 'myissues.html' template
    """
    issue_count_total = Issue.objects.count()

    current_project = request.session.get('current_project', { 'project': 'WINN', 'id': 1 })
    issues = Issue.objects.filter(
            author = request.user,
            project__pk = current_project['id'],
        ).order_by('-created_date')

    issue_count_filter = issues.count()

    context = {
        'issue_count_total': issue_count_total,
        'issue_count_filter': issue_count_filter,
        'issues': issues,
        'filter_name': "Reported by me",
        'refresh_url': reverse('itrac:issues_reported_by_me'),
    }

    return render(request, "itrac/issues.html", context)


@login_required()
def issues_reported_by_me2(request):
    """
    Create a view that will return a list
    of current user's Issues and render them to the 'myissues.html' template
    """
    issue_count_total = Issue.objects.count()

    user = request.user
    issues = Issue.objects.filter(author=user).order_by('-created_date')

    issue_count_filter = issues.count()

    context = {
        'issue_count_total': issue_count_total,
        'issue_count_filter': issue_count_filter,
        'issues': issues,
        'filter_name': "Reported by me2(TEST)"
    }

    return render(request, "itrac/issues_list_collapse.html", context)


@login_required()
def filtered_issues(request, filter):
    """
    Create a view that will return a list of "All issues" or "Open Issues"
    filter: 'all' or 'open'
    """
    issue_count_total = Issue.objects.count()

    issues = None
    filter_name = ''
    refresh_url = None

    current_project = request.session.get('current_project', { 'project': 'WINN', 'id': 0 })

    if filter == "all":
        filter_name = 'All Issues'
        issues = Issue.objects.filter(project__pk=current_project['id']).order_by('-created_date')
        refresh_url = 'itrac:filtered_issues_all'

    elif filter == "open":
        filter_name = 'All Open Issues'
        issues = Issue.objects.filter(
                    status__in=(ISSUE_STATUS.OPEN,),
                    project__pk=current_project['id']
                ).order_by('-created_date')
        refresh_url = 'itrac:filtered_issues_open'

    issue_count_filter = issues.count()

    context = {
        'issue_count_total': issue_count_total,
        'issue_count_filter': issue_count_filter,
        'issues': issues,
        'filter_name': filter_name,
        'refresh_url': reverse(refresh_url),
    }

    return render(request, "itrac/issues.html", context)


@login_required()
def issues_with_tag(request):
    """
    Create a view that will return a list
    of current user's Issues and render them to the 'myissues.html' template
    """
    issue_count_total = Issue.objects.count()

    tag = request.GET['tag']
    issues = Tag.objects.filter(title=tag)[0].issues.all().order_by('-created_date')

    issue_count_filter = issues.count()

    context = {
        'issue_count_total': issue_count_total,
        'issue_count_filter': issue_count_filter,
        'issues': issues,
        'filter_name': f"Issues with tag '{ tag }'"
    }

    return render(request, "itrac/issues.html", context)


@login_required()
def issue_detail(request, pk):
    """
    Create a view that returns a single
    Issue object based on the issue ID (pk) and
    render it to the 'issuedetail.html' template.
    Or return a 404 error if the issue is
    not found
    """
    issue = get_object_or_404(Issue, pk=pk)
    comments = Comment.objects.filter(issue=pk, active_ind=True, active_status_cd=ACTIVE_STATUS.ACTIVE)

    context = {
        'issue': issue,
        'comments': comments,
        'btn_expand_disabled': True,   # disable the expand button as it is fullscreen already
    }

    return render(request, "itrac/issue_detail.html", context)


@login_required()
def clone_issue(request, pk):
    """
    Clone an issue
    """
    issue = get_object_or_404(Issue, pk=pk)

    cloned_issue = get_object_or_404(Issue, pk=pk)
    cloned_issue.pk = None    # set to None to get auto generated key
    cloned_issue.title = "CLONE: " + issue.title
    cloned_issue.author = request.user
    cloned_issue.status = ISSUE_STATUS.OPEN
    cloned_issue.save(False)

    # Tags
    cloned_issue.tags.set(issue.tags.all())

    cloned_issue.save()

    # Clone the associated Tags if any
    for att in IssueAttachment.objects.filter(issue=issue):
        att.pk = None
        att.issue = cloned_issue
        att.uploaded_by = request.user
        att.save()

    # Handle the linked issues
    for iss_link in IssueToIssueLink.objects.filter(linked_from_issue=issue):
        iss_link.pk = None
        iss_link.linked_from_issue = cloned_issue
        iss_link.save()

    for iss_link in IssueToIssueLink.objects.filter(linked_to_issue=issue):
        iss_link.pk = None
        iss_link.linked_to_issue = cloned_issue
        iss_link.save()

    new_issue_link = IssueToIssueLink(
                linked_from_issue = cloned_issue,
                link_from_type = ISSUE_LINK_TYPE.CLONES,
                linked_to_issue = issue,
                updated_by = request.user
            )
    new_issue_link.save()

    return redirect('itrac:issue_detail', cloned_issue.pk)


@login_required()
def issue_detail_partial(request, pk):
    """
    Create a view that returns a single
    Issue object based on the issue ID (pk) and
    render it to the 'issuedetail.html' and issue.html templates.
    Or return a 404 error if the issue is not found
    """
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    comments = Comment.objects.filter(issue=pk).order_by('created_date')

    user = request.user
    issue = Issue.objects.get(pk=pk)
    try:
        savedissue = SavedIssue.objects.get(user=user, issue=issue)
        favourite = True
    except SavedIssue.DoesNotExist:
        savedissue = None
        favourite = False

    context = {
        'issue': issue,
        'comments': comments,
        'favorite': favourite,
    }
    data['html_issue_detail'] = render_to_string('includes/partial_issue_details.html', context, request=request)

    return JsonResponse(data)


@login_required()
def upvote(request, pk):
    data = dict()
    issue = Issue.objects.get(pk=pk)
    issue.upvotes += 1
    issue.save()
    # notify.send(request.user, recipient=issue.author, verb="upvoted your Issue: " + issue.title)
    # messages.success(request, 'Issue upvoted!')
    data['upvotes'] = issue.upvotes
    data['status'] = 'S'
    return JsonResponse(data)


@login_required()
def purchase_vote(request, pk):
    issue = Issue.objects.get(pk=pk)
    issue.upvotes += 1
    issue.save()
    # notify.send(request.user, recipient=issue.author, verb="upvoted your Issue: " + issue.title)
    messages.success(request, 'Issue upvoted!')
    return redirect('itrac:issue_detail', pk)


@login_required()
def create_issue(request):
    """
    Create a view that allows us to create an issue depending if the Issue ID
    is null or not
    """
    if request.method == "POST":
        form = IssueCreateForm(request.POST, request.FILES)
        if form.is_valid():

            form.instance.author = request.user
            form.instance.updated_by = request.user

            if form.instance.issue_type == 'FEATURE':
                form.instance.price = 100
            else:
                form.instance.price = 0
            issue = form.save()

            return redirect('itrac:issue_detail', issue.pk)
    else:
        # Project is default to current_project
        current_project = request.session.get('current_project', { 'project': 'WINN', 'id': 0 })
        form = IssueCreateForm(
            initial = { 'project': current_project['id'] }
        )

    return render(request, 'itrac/issue_create.html', {'form': form})


@login_required()
def edit_issue(request, pk):
    """
    Create a view that allows us to edit a issue depending if the Issue ID
    is null or not
    """
    issue = get_object_or_404(Issue, pk=pk)
    user = request.user
    # Prevents a non-staff user from editing another users comment
    if not request.user.is_staff:
        if user != request.user:
            messages.success(
                request,
                'You Do Not Have Permission To Edit this Issue'
            )
            return redirect('itrac:issue_detail', issue.pk)

    if request.method == "POST":
        form = IssueEditForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():

            form.instance.updated_by = request.user

            if form.instance.issue_type == 'FEATURE':
                form.instance.price = 100
            else:
                form.instance.price = 0

            issue = form.save()
            # notify.send(request.user, recipient=issue.author, verb="updated your Issue: " + issue.title)
            messages.success(request, 'Issue Edited with success!')

            return redirect('itrac:issue_detail', issue.pk)
    else:
        form = IssueEditForm(instance=issue)

    return render(request, 'itrac/issue_edit.html', {'form': form})


@login_required
@require_GET
def description_raw_markdown(request, pk):
    """
     return the raw markdown of the description field of the issue
    """
    issue = get_object_or_404(Issue, pk=pk)
    data = {
        'description': issue.description,
    }
    return JsonResponse(data)


@login_required
@require_GET
def description_as_html(request, pk):
    """
     return the raw markdown of the description field of the issue
    """
    issue = get_object_or_404(Issue, pk=pk)
    data = {
        'description': issue.description,
    }
    return JsonResponse(data)


@login_required
@require_POST
def edit_description(request, pk):
    """
    Create a view that allows us to create
    or edit a comment depending if the Comment ID
    is null or not
    """
    issue = get_object_or_404(Issue, pk=pk)

    form = IssueEditDescriptionForm(request.POST, instance=issue)
    if form.is_valid():
        form.instance.updated_by = request.user
        form.save()
        resp = { 'status': 'S', }         # 'S': successful, 'F': Failed
    else:
        resp = {
            'status': 'F',         # 'S': successful, 'F': Failed
            'error': "error",
        }

    return JsonResponse(resp)


@login_required()
@require_POST
def issue_change_status(request, pk):
    """
    Change the status of the issue, also log tracking information
    """
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)
    new_status = request.POST['new_status']
    issue.status = ISSUE_STATUS[new_status]
    issue.save()

    # Reload issue status post change
    issue = get_object_or_404(Issue, pk=pk)
    data['issue_status'] = issue.get_status_display()
    data['status'] = 'S'

    # TO ADD status change tracking later

    return JsonResponse(data)


@login_required()
def change_assignee_users(request, pk):
    """
    Return a list of users to be choices for assginee
    """
    data = dict()

    users = get_user_model().objects.all()
    context = {
        'issue_id': pk,
        'users': users,
    }

    data['html_user_list'] = render_to_string('includes/partial_issue_details_user_list.html', context, request=request)
    data['status'] = 'S'

    # TO ADD status change tracking later

    return JsonResponse(data)

@login_required()
def change_assignee_change(request, pk, user_pk):
    """
    Update the database the selected user
    """
    data = dict()

    issue = get_object_or_404(Issue, pk=pk)
    if user_pk > 0:
        user = get_object_or_404(get_user_model(), pk=user_pk)
    else:
        user = None   # unassign

    issue.assignee = user
    issue.save()

    data['status'] = 'S'

    # TO ADD status change tracking later

    return JsonResponse(data)
