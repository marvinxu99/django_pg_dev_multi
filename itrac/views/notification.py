import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.http import require_POST

from ..filters import IssueFilter
from ..models import ISSUE_STATUS, Comment, Issue, SavedIssue, Tag


def my_notifications(request):
    """
    Create a view that will return a list
    of notifications for the user to the 'notifications.html' template
    """

    user = request.user
    notifications = Notification.objects.unread().filter(recipient=user).order_by('-timestamp')
    return render(request, "itrac/notifications.html", {'notifications': notifications})
