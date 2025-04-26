from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('app:home')
        else:
            messages.error(request, 'Hubo un error en el registro. Revisa los campos.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

from django.contrib import messages  # Asegúrate de importar messages

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('app:assistant')
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos. Por favor, intenta de nuevo.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('app:home')  # Redirigir al home después de cerrar sesión
