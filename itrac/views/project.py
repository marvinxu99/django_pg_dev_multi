from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from ..models import Project
from ..forms import ProjectForm


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'itrac/project/project_list.html', { 'projects': projects })

def save_project_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            projects = Project.objects.all()
            data['html_project_list'] = render_to_string('itrac/project/partial_project_list.html', {
                'projects': projects
            })
        else:
            data['form_is_valid'] = False
    
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def project_create(request):
    data = dict()
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.updated_by = request.user
            project.save()

            data['form_is_valid'] = True
            projects = Project.objects.all()
            data['html_project_list'] = render_to_string('itrac/project/partial_project_list.html', {
                'projects': projects
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ProjectForm()

    context = {'form': form}
    data['html_form'] = render_to_string('itrac/project/partial_project_create.html', context, request=request)

    return JsonResponse(data)


def project_edit(request, pk):
    data = dict()

    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            project = form.save(commit=False)
            project.updated_by = request.user
            project.save()

            data['form_is_valid'] = True
            projects = Project.objects.all()
            data['html_project_list'] = render_to_string('itrac/project/partial_project_list.html', {
                'projects': projects
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ProjectForm(instance=project)

    context = {'form': form}
    data['html_form'] = render_to_string('itrac/project/partial_project_edit.html', context, request=request)

    return JsonResponse(data)


def project_delete(request, pk):
    pass