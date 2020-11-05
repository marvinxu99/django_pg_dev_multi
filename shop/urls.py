from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.shop_home, name='shop_home'), 
    path('shop_data/load', views.load_shop_data, name='load_shop_data'), 

    path('product/<str:prod_cat>/', views.get_product_by_category, name='product_by_category'), 
    path('product/<int:pk>/cart_add/', views.add_to_cart, name='add_to_cart'), 

]
