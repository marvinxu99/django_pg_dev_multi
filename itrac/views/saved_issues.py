import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, reverse

from ..models import Issue, SavedIssue


@login_required()
def my_saved_issues(request):
    """
    Create a view that will return a list
    of current user's Saved Issues (favourite issues) and render them to the 'issues.html' template
    """
    issue_count_total = Issue.objects.count()

    user = request.user
    saved_issues = SavedIssue.objects.filter(user=user).order_by('-created_date')
    issues = []
    for saved_issue in saved_issues:
        issues.append(saved_issue.issue)

    issue_count_filter = saved_issues.count()

    context = {
        'issue_count_total': issue_count_total,
        'issue_count_filter': issue_count_filter,
        'issues': issues,
        'filter_name': "My Favorite Issues",
        'refresh_url': reverse('itrac:my_saved_issues'),
    }

    return render(request, "itrac/issues.html", context)


@login_required
@require_POST
def save_issue_favourite(request, pk):
    '''
    handle Add to or Remove from favourites
    '''
    favourite_action = request.POST['favourite_action']

    if favourite_action == "add":
        resp = save_issue_as_favourite(request, pk)
    else:
        resp = remove_from_favourites(request, pk)

    return JsonResponse(resp)


def save_issue_as_favourite(request, pk):
    '''
    Helper function - Save an issue as favourite
    '''
    data = dict()
    data['status'] = 'S'

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
        data['message']= 'Issue added to your Saved Issues!'
    else:
        messages.error(request, 'Issue already added in your Saved Issues!')
        data['message']= 'Issue already added in your Saved Issues!'

    return data


def remove_from_favourites(request, pk):
    '''
    Helper function - Remove issue from favourites
    '''
    data = dict()
    data['status'] = 'S'

    user = request.user
    issue = Issue.objects.get(pk=pk)

    try:
        savedissue = SavedIssue.objects.get(user=user, issue=issue)
        savedissue.delete()
        messages.success(request, 'Saved Issue deleted!')
    except Exception as e:
        data['status'] = 'F'
        data['message'] = str(e)

    return data
