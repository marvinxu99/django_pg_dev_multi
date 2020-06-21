from django.urls import path, include, re_path

from . import views


app_name = 'scan_n_pay'
urlpatterns = [
    path('scan/', views.scan_n_pay, name='scan_n_pay'),
    path('scan/get_item/<str:barcode>/', views.get_item, name='get_item'),

    path('pay_successful/', views.pay_successful, name='pay_successful'),

]
