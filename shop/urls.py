from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.shop_home, name='shop_home'), 
    path('shop_data/load', views.load_shop_data, name='load_shop_data'), 

    path('product/<str:prod_cat>/', views.get_product_by_category, name='product_by_category'), 

    path('cartitem/<int:pk>/add/', views.cart_add_item, name='cart_add_item'), 
    path('cartitem/<int:pk>/deduct/', views.cart_deduct_item, name='cart_deduct_item'), 
    path('cartitem/<int:pk>/remove/', views.cart_remove_item, name='cart_remove_item'), 

    path('cart/item_count/', views.cart_item_count, name='cart_item_count'), 
    path('cart/items/', views.cart_view_items, name='cart_view_items'), 
    path('cart/remove_all/', views.cart_remove_all_items, name='cart_remove_all_items'), 
    path('cart/pay/success/', views.cart_pay_success,  name='stripe_pay_success'),
    path('cart/pay/cancelled/', views.cart_pay_cancelled,  name='stripe_pay_cancelled'),

    path('orders/view/', views.view_orders,  name='view_orders'),
    path('orders/view/filter/', views.view_orders_filter,  name='view_orders_filter'),
    path('orders/view/orderid/<int:orderid>/', views.view_orders_orderid,  name='view_orders_orderid'),

    path('stripe/config/', views.stripe_config, name='stripe_config'), 
    path('stripe/checkout/', views.create_checkout_session, name='stripe_checkout'),
    path('stripe/success/', views.SuccessView.as_view(),  name='stripe_success'),
    path('stripe/cancelled/', views.CancelledView.as_view(), name='stripe_cancelled'), 

]
