from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.order_payment, name='order_payment'),
    path('plant-details/<str:plant_name>/', views.plant_details, name='plant_details'),
    path('add-to-cart/<str:plant_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('cart/decrease/<int:item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('houseplants/', views.houseplants, name='houseplants'),
    path('search/', views.search_plants, name='search_plants'),
]