from django.urls import path

from . import views

app_name = 'scan_n_pay'
urlpatterns = [
    path('scan/', views.scan_n_pay, name='scan_n_pay'),
    path('scan/get_item/', views.get_item, name='get_item'),
    path('scan/transdata/', views.save_trans_data, name='trans_data'),
    path('scan/products/', views.search_products, name='search-products'),

    path('stripe/config/', views.stripe_config, name='stripe_config'),
    path('stripe/checkout/', views.create_checkout_session, name='stripe_checkout'),
    path('stripe/success/', views.SuccessView.as_view(),  name='stripe_success'),
    path('stripe/cancelled/', views.CancelledView.as_view(), name='stripe_cancelled'),

]
