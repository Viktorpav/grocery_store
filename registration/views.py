from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            registration = form.cleaned_data.get('registration')
            messages.success(request, f'Account created for {registration}! ')
            return redirect('food-main')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



