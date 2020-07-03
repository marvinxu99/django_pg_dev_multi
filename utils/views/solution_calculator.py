from django.shortcuts import render

def solution_calculator(request):
    return render(request, 'utils/solution_calculator.html')
