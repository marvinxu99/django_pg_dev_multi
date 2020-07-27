import os
import requests
from datetime import datetime, timedelta, time
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Count, Q
from django.core import serializers
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
import json


from ..models import Issue, Comment, Reply, SavedIssue, Tag, ISSUE_STATUS
from ..forms import IssueForm, CommentForm, ReplyForm
from ..filters import IssueFilter


def report(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    completed_daily = Issue.objects.filter(resolved_date__gte=today_start).filter(resolved_date__lt=today_end).count()

    this_week_start = datetime.combine(today - timedelta(7), time())
    completed_weekly = Issue.objects.filter(resolved_date__gte=this_week_start).filter(resolved_date__lt=today_end).count()

    this_month_start = datetime.combine(today - timedelta(28), time())
    completed_monthly = Issue.objects.filter(resolved_date__gte=this_month_start).filter(resolved_date__lt=today_end).count()
    print(completed_daily)

    return render(request, "itrac/report.html", {'completed_daily': str(completed_daily), 'completed_weekly': str(completed_weekly), 'completed_monthly': str(completed_monthly)})


def do_search_my(request):
    """
    Create a view for searching my issues by keyword search on Issue.Title to return a list
    of matching Issues and render them to the 'myissues.html' template
    """
    user = request.user
    issues = Issue.objects.filter(author=user).filter(title__icontains=request.GET['q'])
    return render(request, "itrac/myissues.html", {"issues": issues})


def do_search(request):
    """
    Create a view for searching all issues by keyword search on Issue.Title to return a list
    of matching Issues and render them to the 'issues.html' template
    """
    issues = Issue.objects.filter(title__icontains=request.GET['q'])

    issue_count_total = Issue.objects.count()
    issue_count_filter = issues.count()

    filter_name = f'''Issue title contains "{ request.GET['q']}" '''

    context = {
            'issue_count_total': issue_count_total,
            'issue_count_filter': issue_count_filter,
            'issues': issues,
            'filter_name': filter_name,
        }

    return render(request, "itrac/issues.html", context)


@login_required
def issues_assigned_to_me(request):
    """
    Create a view that will return a list
    of Issues assigned to the current user.
    """
    issue_count_total = Issue.objects.count()

    issues = Issue.objects.filter(assignee=request.user).order_by('-created_date')

    issue_count_filter = issues.count()

    
    context = {
            'issue_count_total': issue_count_total,
            'issue_count_filter': issue_count_filter,
            'issues': issues,
            'filter_name': "My Open Issues",
        }

    return render(request, "itrac/issues.html", context)


@login_required()
def issues_reported_by_me(request):
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
        'filter_name': "Reported by me"
    }

    return render(request, "itrac/issues.html", context)


@login_required()
def issues_reported_by_me2(request):
    """
    Create a view that will return a list
    of current user's Issues and render them to the 'myissues.html' template
    """
    user = request.user
    issues = Issue.objects.filter(author=user).order_by('-created_date')

    issue_count_total = Issue.objects.count()
    issue_count_filter = issues.count()

    context = {
        'issue_count_total': issue_count_total,
        'issue_count_filter': issue_count_filter,
        'issues': issues,
        'filter_name': "Reported by me2"
    }

    return render(request, "itrac/issues_list_collapse.html", context)

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
def saved_issues(request):
    """
    Create a view that will return a list
    of current user's Saved Issues and render them to the 'issues.html' template
    """
    user = request.user
    savedissues = SavedIssue.objects.filter(user=user).order_by('-created_date')
    return render(request, "itrac/savedissues.html", {'savedissues': savedissues})


def my_notifications(request):
    """
    Create a view that will return a list
    of notifications for the user to the 'notifications.html' template
    """

    user = request.user
    notifications = Notification.objects.unread().filter(recipient=user).order_by('-timestamp')
    return render(request, "itrac/notifications.html", {'notifications': notifications})


def get_issue_type_json(request):
    dataset = Issue.objects \
        .values('issue_type') \
        .exclude(issue_type='') \
        .annotate(total=Count('issue_type')) \
        .order_by('issue_type')

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Issue Type'},
        'xAxis': {'type': "category"},
        'series': [{
            'name': 'Issue Type',
            'data': list(map(lambda row: {'name': [row['issue_type']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


def get_status_json(request):
    dataset = Issue.objects \
        .values('status') \
        .exclude(status='') \
        .annotate(total=Count('status')) \
        .order_by('status')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Issue Status'},
        'series': [{
            'name': 'Issue Status',
            'data': list(map(lambda row: {'name': [row['status']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)

def get_bug_upvotes_json(request):
    dataset = Issue.objects \
        .filter(issue_type='BUG') \
        .values('upvotes', 'title') \
        .exclude(upvotes=0) \
        .order_by('upvotes')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Top Bug Upvotes'},
        'series': [{
            'name': 'Issue Upvotes',
            'data': list(map(lambda row: {'name': [row['title']], 'y': row['upvotes']}, dataset))
        }]
    }

    return JsonResponse(chart)

def get_feature_upvotes_json(request):
    dataset = Issue.objects \
    .filter(issue_type='FEATURE') \
    .values('upvotes', 'title') \
    .exclude(upvotes=0) \
    .order_by('upvotes')

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Top Feature Upvotes'},
        'series': [{
            'name': 'Issue Upvotes',
            'data': list(map(lambda row: {'name': [row['title']], 'y': row['upvotes']}, dataset))
        }]
    }

    return JsonResponse(chart)


@login_required()
def search(request):
    issue_list = Issue.objects.all()
    issue_filter = IssueFilter(request.GET, queryset=issue_list)
    return render(request, 'itrac/search_issues.html', {'filter': issue_filter})


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
    comments = Comment.objects.filter(issue=pk)
    comment_replies = []
    for comment in comments:
        replies = Reply.objects.filter(comment=comment)
        comment_replies.append(replies)

    context = {
        'issue': issue, 
        'comments': comments, 
        'comment_replies': comment_replies
    }

    return render(request, "itrac/issue_detail.html", context)


@login_required()
def issue_detail_partial(request, pk):
    """
    Create a view that returns a single
    Issue object based on the issue ID (pk) and
    render it to the 'issuedetail.html' template.
    Or return a 404 error if the issue is
    not found
    """
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    comments = Comment.objects.filter(issue=pk)
    comment_replies = []
    for comment in comments:
        replies = Reply.objects.filter(comment=comment)
        comment_replies.append(replies)

    context = {
        'issue': issue, 
        'comments': comments, 
        'comment_replies': comment_replies
    }

    data['html_issue_detail'] = render_to_string('includes/partial_issue_details.html', context, request=request)

    return JsonResponse(data)


@login_required()
def upvote(request, pk):
    issue = Issue.objects.get(pk=pk)
    issue.upvotes += 1
    issue.save()
    # notify.send(request.user, recipient=issue.author, verb="upvoted your Issue: " + issue.title)
    messages.success(request, 'Issue upvoted!')
    return redirect('itrac:issue_detail', pk)

@login_required()
def save_issue(request, pk):
    user = request.user
    issue = Issue.objects.get(pk=pk)
    try:
        savedissue = SavedIssue.objects.get(user=user, issue=issue)
    except SavedIssue.DoesNotExist:
        savedissue = None
    if savedissue is None:
        savedissue = SavedIssue(user=user, issue=issue)
        savedissue.save()
        messages.success(request, 'Issue added to your Saved Issues!')
    else:
        messages.error(request, 'Issue already added in your Saved Issues!')
    return redirect('itrac:issue_detail', pk)

@login_required()
def delete_saved_issue(request, pk):
    savedissue = SavedIssue.objects.get(pk=pk)
    savedissue.delete()
    messages.success(request, 'Saved Issue deleted!')
    return redirect('saved_issues')


@login_required()
def create_issue(request):
    """
    Create a view that allows us to create an issue depending if the Issue ID
    is null or not
    """
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.instance.author = request.user
            if form.instance.issue_type == 'FEATURE':
                form.instance.price = 100
            else:
                form.instance.price = 0
            issue = form.save()
            
            return redirect('itrac:issue_detail', issue.pk)
    else:
        form = IssueForm()
        
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
        form = IssueForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():

            form.instance.author = request.user
            if form.instance.issue_type == 'FEATURE':
                form.instance.price = 100
            else:
                form.instance.price = 0
            issue = form.save()
            # notify.send(request.user, recipient=issue.author, verb="updated your Issue: " + issue.title)
            messages.success(request, 'Issue Edited with success!')

            return redirect('itrac:issue_detail', issue.pk)
    else:
        form = IssueForm(instance=issue)

    return render(request, 'itrac/issue_edit.html', {'form': form})


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
def create_or_edit_reply(request, issue_pk, comment_pk, pk=None):
    """
    Create a view that allows us to create
    or edit a reply depending if the Reply ID
    is null or not
    """
    comment = get_object_or_404(Comment, pk=comment_pk)
    reply = get_object_or_404(Reply, pk=pk) if pk else None
    if request.method == "POST":
        form = ReplyForm(request.POST, request.FILES, instance=reply)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.comment = comment
            form.save()
            # notify.send(request.user, recipient=comment.author, verb="added a reply to your Comment: " + comment.comment)
            messages.success(request, 'Reply Saved!')
            return redirect('itrac:issue_detail', issue_pk)
    else:
        form = ReplyForm(instance=reply)
    return render(request, 'itrac/replyform.html', {'form': form})



