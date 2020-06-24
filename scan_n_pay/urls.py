from django.urls import path

from . import views

app_name = 'scan_n_pay'
urlpatterns = [
    path('scan/', views.scan_n_pay, name='scan_n_pay'),
    path('scan/get_item/<str:barcode>/', views.get_item, name='get_item'),
    path('scan/get_item/', views.get_item, name='get_item'),
    path('scan/transdata/', views.trans_data, name='trans_data'),

    path('pay/config/', views.stripe_config, name='config'), 
    path('pay/create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('pay/success/', views.SuccessView.as_view(),  name='paysuccess'),
    path('pay/cancelled/', views.CancelledView.as_view(), name='paycancelled'), 

]
