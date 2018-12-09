from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import MenuForm

def main(request):
    return render(request, 'food/main.html')

def menu(request):
    form = MenuForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'food/menu.html', context) # {'title': 'Menu'}   {'content': ["If you would like to order by phone or contact us by email, please", "wsiz@students.pl", "+48111111111"]})

