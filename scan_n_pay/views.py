from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps

def scan_n_pay(request): 
    # print("app: " + apps.get_app_config('scan_n_pay').name)
    for app in apps.get_app_configs():
        #print(app.name, app.verbose_name, app.label, app.path)
        print(app.label)

    return render(request, 'scan_n_pay/scan_n_pay.html')


def pay_successful(request):
    return render(request, 'scan_n_pay/pay_successful.html')