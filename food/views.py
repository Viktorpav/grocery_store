from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def main(request):
    return render(request, 'food/main.html')

def menu(request):
    return render(request, 'food/menu.html', {'title': 'Menu'}) #{'content': ["If you would like to order by phone or contact us by email, please", "wsiz@students.pl", "+48111111111"]})


