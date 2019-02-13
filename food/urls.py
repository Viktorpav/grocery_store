from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='food-main'),
    path('product/<product_id>', views.product, name='product'),
    path('menu/', views.menu, name='food-menu'),
]
