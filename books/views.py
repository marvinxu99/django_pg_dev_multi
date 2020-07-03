from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from .models import Book
from .forms import BookForm

# List all the books created.
def book_list(request):
    books = Book.objects.all()    
    return render(request, 'books/book_list.html', {'books': books})


# Create a new book
def book_create(request):
    data = dict()

    print("ajax call recieved.")

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            
            data['form_is_valid'] = True
            
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
                'books': books
            })
            
        else:
            data['form_is_valid'] = False
    else:
        # form = BookForm()
        form = BookForm(initial={ 'publication_date': datetime.date.today() } )

    context = {'form': form}
    data['html_form'] = render_to_string('books/includes/partial_book_create.html',
        context,
        request=request,
    )
     
    return JsonResponse(data)
    