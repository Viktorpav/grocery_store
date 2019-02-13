from django.urls import path
from . import views

urlpatterns = [
    #path('', views.main, name='food-main'),
    #path('menu/', views.menu, name='food-menu'),
    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),

]
