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


from ..models import Issue, Comment, SavedIssue, Tag, ISSUE_STATUS
from ..filters import IssueFilter


def my_notifications(request):
    """
    Create a view that will return a list
    of notifications for the user to the 'notifications.html' template
    """

    user = request.user
    notifications = Notification.objects.unread().filter(recipient=user).order_by('-timestamp')
    return render(request, "itrac/notifications.html", {'notifications': notifications})
