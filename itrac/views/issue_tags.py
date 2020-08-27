from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from ..models import Tag
from ..forms import TagCreateForm, TagEditForm


@login_required
def edit_issue_tags(request, pk):
    pass
    # tags = Tag.objects.all()
    # return render(request, 'itrac/tag/tag_list.html', { 'tags': tags })


