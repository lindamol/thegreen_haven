from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('payment/', views.payment, name='payment'),
    path('plant-details/<str:plant_name>/', views.plant_details, name='plant_details'),
]