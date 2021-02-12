from django.urls import path

from . import views


app_name = 'payments'
urlpatterns = [
    path('demo/', views.DemoView.as_view(), name='demo'),
    path('config/', views.stripe_config, name='config'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancelled/', views.CancelledView.as_view(), name='cancelled'),
]
