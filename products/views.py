from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from .models import Producto, Order, OrderItem


def es_admin(user):
    return user.is_staff


def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})


@login_required
@user_passes_test(es_admin)
def product_create(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto creado correctamente.')
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'titulo': 'Nuevo producto'})


@login_required
@user_passes_test(es_admin)
def product_edit(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto actualizado.')
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar producto'})


@login_required
@user_passes_test(es_admin)
def product_delete(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado.')
    return redirect('home')


# ---------- CARRITO ----------

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    messages.success(request, 'Producto agregado al carrito.')
    return redirect('home')


def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid, cantidad in cart.items():
        try:
            producto = Producto.objects.get(id=pid)
        except Producto.DoesNotExist:
            continue
        subtotal = producto.precio * cantidad
        total += subtotal
        items.append({'producto': producto, 'cantidad': cantidad, 'subtotal': subtotal})
    return render(request, 'cart.html', {'productos': items, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    messages.success(request, 'Producto quitado del carrito.')
    return redirect('view_cart')


def update_cart(request, product_id):
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        cart = request.session.get('cart', {})
        if cantidad > 0:
            cart[str(product_id)] = cantidad
        else:
            cart.pop(str(product_id), None)
        request.session['cart'] = cart
        messages.success(request, 'Cantidad actualizada.')
    return redirect('view_cart')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Tu carrito está vacío.')
        return redirect('view_cart')

    # Crear la orden
    order = Order.objects.create(usuario=request.user, total=0)
    total = 0

    for pid, cantidad in cart.items():
        try:
            producto = Producto.objects.get(id=pid)
        except Producto.DoesNotExist:
            continue
        subtotal = producto.precio * cantidad
        total += subtotal
        OrderItem.objects.create(
            order=order,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=producto.precio,
        )

    order.total = total
    order.save()

    # Vaciar el carrito
    request.session['cart'] = {}
    messages.success(request, f'¡Compra confirmada! Tu orden es la #{order.id}.')
    return redirect('order_detail', order_id=order.id)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, usuario=request.user)
    return render(request, 'order_detail.html', {'order': order})