from django.http import HttpResponseRedirect
from django.shortcuts import render

def scan_n_pay(request):
    return render(request, 'scan_n_pay/scan_n_pay.html')


def pay_successful(request):
    return render(request, 'scan_n_pay/pay_successful.html')