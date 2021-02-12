from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required

from catalog.forms import ChangeBookStatusStaffModelForm
from catalog.models import BookInstance


@permission_required('catalog.can_mark_returned')
def change_book_status_staff(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ChangeBookStatusStaffModelForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.status = form.cleaned_data['status']
            book_instance.save()

            # redirect to a new URL: ??TODO solve the circular import issue??
            #return HttpResponseRedirect(reverse('catalog:book-detail', book_instance.book.pk ) )
            return HttpResponseRedirect(reverse('catalog:books'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ChangeBookStatusStaffModelForm()

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/change_book_status_staff.html', context)
