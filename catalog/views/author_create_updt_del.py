# Create, Update, Delete
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin

from catalog.models import Author


class AuthorCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.add_author'
    model = Author
    template_name = 'catalog/author_create.html'
    fields = '__all__'
    initial = {'date_of_birth': datetime.date.today()}
    success_url = reverse_lazy('catalog:authors')

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.change_author'
    model = Author
    template_name = 'catalog/author_update.html'
    success_url = reverse_lazy('catalog:authors')
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_author'
    model = Author
    success_url = reverse_lazy('catalog:authors')

    '''
    if you want to name the comfirm tempalte to "author_check_delete.html", then
    template_name_suffix ="_check_delete"
    The DeleteView page displayed to a GET request uses a template_name_suffix of '_confirm_delete'.
    For example, changing this attribute to '_check_delete' for a view deleting objects for the
    example Author model would cause the default template_name to be 'myapp/author_check_delete.html'.
    '''
