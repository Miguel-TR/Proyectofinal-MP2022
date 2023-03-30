from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .forms import ContactoForm

from productos.forms import ProductoForm
from productos.models import Producto
from productos.models import Contacto
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
#from .models import Producto
#Carrito
from productos.Carrito import Carrito
from productos.forms import ProductoForm
from productos.models import Producto

#def aboutme(request):
 #   Productos =  Producto.objects.all()
#  return render(request,"productos/aboutme.html",{'misproductos': Productos})

# Create your views here.
class ProductoListView(ListView):    
    model = Producto
    def get_queryset(self):
        query = self.request.GET.get('q')
        print ("query:",query)
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
            print("object_list: ",object_list)
        else:
            object_list = self.model.objects.all()
            print("object_list else: ",object_list)
        return object_list



class ProductoCreate(CreateView):
    model=Producto
    #fields = ['nombre', 'descripcion', 'imagen']
    form_class = ProductoForm
    success_url = reverse_lazy('productos')

class ProductoUpdate(UpdateView):
    model=Producto
    form_class= ProductoForm
    success_url = reverse_lazy('productos')
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('productos')+'?Actualizado'
class ProductoDelete(DeleteView):
    model = Producto
    def get_success_url(self):
        return reverse_lazy('productos')+'?Eliminado'      


class ProductoDetail(DetailView):
    model=Producto
    template_name_suffix = '_detail'

def contacto(request):
    model=Contacto
    data ={
        'form':ContactoForm()
    }

    if request.method=='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] =  formulario

    return render(request,'core/contacto.html', data)

#Carrito
def agregar_producto2(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return render(request, "productos/carrito.html")

def agregar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("productos")

def eliminar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return render(request, "productos/carrito.html")

def restar_producto(request,producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return render(request, "productos/carrito.html")

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('productos')

