from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            registration = form.cleaned_data.get('registration')
            messages.success(request, f'Your account has been created! You are now able to log in{registration}! ')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    return render(request, 'registration/profile.html')
