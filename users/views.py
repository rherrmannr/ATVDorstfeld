from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Benutzer wurde angelegt! Du kannst dich einloggen!')
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})
