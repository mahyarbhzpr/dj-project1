from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from cart.forms import CartAddProductForm
from .cart import Cart
from shop.models import Product
from core.models import imagesite

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, product_count=cd['product_count'], update_count=cd['update'])
        messages.success(request, "محصول با موفقیت به سبد خرید اضافه شد")
    return HttpResponseRedirect(reverse('shop:products'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product_id)
    return redirect('cart:cart_detail')


def cart_detail(request):
    logo = imagesite.objects.get(id=1)
    cart = Cart(request)
    for item in cart:
        item['update_product_count_form'] = CartAddProductForm(initial={'product_count': item['product_count'], 'update': True})
    if not cart:
        return render(request, 'empty-cart.html', {'cart': cart, 'logo': logo})
    return render(request, 'cart_page.html', {'cart': cart, 'logo': logo})