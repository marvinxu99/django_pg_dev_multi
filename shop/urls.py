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

]
