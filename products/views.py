from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})
from .forms import ProductoForm
from django.shortcuts import redirect, get_object_or_404

def product_create(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form})


def product_edit(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form})


def product_delete(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('home')