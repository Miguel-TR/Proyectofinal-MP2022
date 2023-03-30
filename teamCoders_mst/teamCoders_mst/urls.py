"""teamCoders_mst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from core import views
from django.conf import settings
from django.conf.urls.static import static
from productos import views as productos_views
from productos.views import (ProductoListView, ProductoCreate, ProductoUpdate,ProductoDelete,ProductoDetail)

app_name="core"
urlpatterns = [
    path("", views.index, name='index'),
    path('about-me', ProductoListView.as_view(),name='productos'),
    path('create/', ProductoCreate.as_view(),name='create'),
    path('update/<int:pk>', ProductoUpdate.as_view(), name='update'),
    path('delete/<int:pk>', ProductoDelete.as_view(), name='delete'),
    path('detail/<int:pk>', ProductoDetail.as_view(), name='detail'),
    path("acercade/", views.acercade, name='acercade'),
    path("contacto/", productos_views.contacto, name='contacto'),
    path("micuenta/", views.micuenta, name='micuenta'),
    #path('aboutme', productos_views.aboutme),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro', views.registro, name='registro'),
    #Carrito
    path('agregar/<int:producto_id>', productos_views.agregar_producto, name="Add"),
    path('agregar/<int:producto_id>', productos_views.agregar_producto2, name="agregar"),
    path('eliminar/<int:producto_id>', productos_views.eliminar_producto, name="del"),
    path('restar/<int:producto_id>', productos_views.restar_producto, name="sub"),
    path('limpiar/', productos_views.limpiar_carrito, name="CLS"),
    path('carrito/', views.carrito, name='carrito' )
    
 
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


