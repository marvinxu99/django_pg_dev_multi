from django.shortcuts import render
from ..forms import DictionaryForm

def oxford(request):
    search_result = {}
    
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        
        if form.is_valid():
            search_result = form.search()

            print(search_result)
    
    else:
        form = DictionaryForm()

    return render(request, 'utils/oxford.html', {'form': form, 'search_result': search_result})
