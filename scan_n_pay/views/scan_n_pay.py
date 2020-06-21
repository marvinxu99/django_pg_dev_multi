from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps

def scan_n_pay(request): 
    # # print("app: " + apps.get_app_config('scan_n_pay').name)
    # for app in apps.get_app_configs():
    #     #print(app.name, app.verbose_name, app.label, app.path)
    #     print(app.label)


    query = request.GET.get('q')
    if query:
        print("q= " + query)
        
    # if query:
    #     author_list = self.model.objects.filter(
    #         Q(first_name__icontains=query) | Q(last_name__icontains=query)
    #     )
    # else:
    #     author_list = self.model.objects.all()
    # #return Author.objects.filter(name__icontains='war')[:5] # Get 5 books containing the title war
    # return author_list

    return render(request, 'scan_n_pay/scan_n_pay.html')




def pay_successful(request):
    return render(request, 'scan_n_pay/pay_successful.html')