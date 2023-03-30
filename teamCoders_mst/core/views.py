from django.shortcuts import HttpResponse,render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request): 
    return render(request, "core/index.html") 
def acercade(request):
    return render(request, "core/acercade.html")
def contactanos(request):
    return render(request, "core/contacto.html")
def micuenta(request):
    return render(request, "core/micuenta.html")

def carrito(request):
    return render(request, "productos/carrito.html")

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='index')
        data['form']=formulario
    return render(request, 'registration/registro.html', data)

