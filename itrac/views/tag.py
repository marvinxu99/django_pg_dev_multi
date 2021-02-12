from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from ..models import Tag
from ..forms import TagCreateForm, TagEditForm


@login_required
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'itrac/tag/tag_list.html', { 'tags': tags })


@login_required
def tag_create(request):
    data = dict()
    if request.method == 'POST':
        form = TagCreateForm(request.POST)

        if form.is_valid():
            tag = form.save(commit=False)
            tag.created_by = request.user
            tag.updated_by = request.user
            tag.save()

            data['form_is_valid'] = True
            tags = Tag.objects.all()
            data['html_tag_list'] = render_to_string('itrac/tag/partial_tag_list.html', {
                'tags': tags,
                'user': request.user,
            })
        else:
            data['form_is_valid'] = False
    else:
        form = TagCreateForm()

    context = {'form': form}
    data['html_form'] = render_to_string('itrac/tag/partial_tag_create.html', context, request=request)

    return JsonResponse(data)


@login_required
def tag_edit(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    data = dict()

    if request.method == 'POST':
        form = TagEditForm(request.POST, instance=tag)

        if form.is_valid():
            tag = form.save(commit=False)
            tag.updated_by = request.user
            tag.save()

            data['form_is_valid'] = True
            tags = Tag.objects.all()
            data['html_tag_list'] = render_to_string('itrac/tag/partial_tag_list.html', {
                'tags': tags,
                'user': request.user,
            })
        else:
            data['form_is_valid'] = False
    else:
        form = TagEditForm(instance=tag)

    context = {'form': form}
    data['html_form'] = render_to_string('itrac/tag/partial_tag_edit.html', context, request=request)

    return JsonResponse(data)


@login_required
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    data = dict()

    if request.method == 'POST':
        tag.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        tags = Tag.objects.all()
        data['html_tag_list'] = render_to_string('itrac/tag/partial_tag_list.html', {
            'tags': tags,
            'user': request.user,
        })
    else:
        context = {'tag': tag}
        data['html_form'] = render_to_string('itrac/tag/partial_tag_delete.html', context, request=request)

    return JsonResponse(data)
