from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from . import views


app_name = 'scan_n_pay'
urlpatterns = [
    path('scan/', views.scan_n_pay, name='scan_n_pay'),
    path('scan/get_item/<str:barcode>/', views.get_item, name='get_item'),
    path('scan/get_item/', views.get_item, name='get_item'),
    path('pay_successful/', views.pay_successful, name='pay_successful'),
    path('scan/transdata/', csrf_exempt(views.trans_data), name='trans_data'),

]
