from django.shortcuts import render, redirect
from .models import CartItem, Product
from django.contrib.auth.decorators import login_required

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})
