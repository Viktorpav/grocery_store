from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from food.models import *


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_iceCream = products_images.filter(product__category__id=3)
    products_images_drinks = products_images.filter(product__category__id=4)

    return render(request, 'food/home.html', locals())

def menu(request):

    return render(request, 'food/menu.html') # {'title': 'Menu'}   {'content': ["If you would like to order by phone or contact us by email, please", "wsiz@students.pl", "+48111111111"]})

def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request, session_key)


    return render(request, 'food/product.html', locals())