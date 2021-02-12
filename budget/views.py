from django.shortcuts import render

# Create your views here.
def budget_home(request):
    return render(request, 'budget/budget_home.html')
