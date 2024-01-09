from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.cart import Cart
from decimal import Decimal
from zeep import Client
from django.views.generic import TemplateView
from django.conf import settings
import requests
from django.http import FileResponse
from core.models import imagesite, contentsite
from customize.models import *
from .forms import CommentFormshop



def Search(request):
    logo = imagesite.objects.get(id=1)
    cart = Cart(request)
    category = Category.objects.all()
    if request.method == 'GET':
        q = request.GET.get('search')
    products = Product.objects.filter(name__icontains=q)
    return render(request, 'shop.html', {'products': products, 'cart': cart,'category': category,'logo': logo})

def product_list(request):
    cart = Cart(request)
    logo = imagesite.objects.get(id=1)
    content = contentsite.objects.get(id=6)
    sliders = slider.objects.all()
    category = Category.objects.all()
    products = Product.objects.all().order_by('-date_created')
    context = {'products': products, 'cart': cart,'category': category, 'slider': sliders,'logo': logo, 'content': content}
    return render(request, "shop.html", context)
    
def product_listbuy(request):
    cart = Cart(request)
    logo = imagesite.objects.get(id=1)
    products = Product.objects.all().order_by('-countofbuy')
    context = {'products': products, 'cart': cart,'logo': logo,}
    return render(request, "shopbuy.html", context)
    
def product_listpopular(request):
    cart = Cart(request)
    logo = imagesite.objects.get(id=1)
    products = Product.objects.filter(ratings__isnull=False).order_by('-ratings__average')
    context = {'products': products, 'cart': cart,'logo': logo,}
    return render(request, "shoppopular.html", context)
    
def product_listmostview(request):
    cart = Cart(request)
    logo = imagesite.objects.get(id=1)
    products = Product.objects.all().order_by('-viewscount')
    context = {'products': products, 'cart': cart,'logo': logo,}
    return render(request, "shopmostview.html", context)


@login_required()
def download_file(request, slug):
    try:
        product = Product.objects.get(slug=slug)

        userProduct = UserProduct.objects.filter(product=product, user=request.user)

        return FileResponse(open(product.file.path, "rb"))

    except UserProduct.DoesNotExist:
        return redirect("customuser:register_view")

def products_category(request, slug):
    cart = Cart(request)
    logo = imagesite.objects.get(id=1)
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category__slug=category.slug).order_by('-date_created')
    context = {'products': products, 'cart': cart,'logo': logo}
    return render(request, 'shopcat.html', context)

def product_details(request, slug):
    logo = imagesite.objects.get(id=1)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    product = get_object_or_404(Product, slug=slug)
    product.viewscount=product.viewscount+1
    product.save()
    productss = Product.objects.filter(category=product.category)
    comments = ShopComment.objects.filter(product=product)
    commentscount = ShopComment.objects.filter(product=product, active=True).count()
    if request.method == 'POST':
        form = CommentFormshop(request.POST or None)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_phone = form.cleaned_data["phone"]
            new_description = form.cleaned_data["description"]

            new_comment = ShopComment(product=product, name=new_name,phone=new_phone,description=new_description)
            new_comment.save()
            form = CommentFormshop(request.POST)
    context = {'product': product, 'productss': productss,'logo': logo, 'comment': comments,'css': css, 'js': js, 'commentcount': commentscount}
    return render(request, "product.html", context)

@login_required
def checkout(request):
    cart = Cart(request)
    logo = imagesite.objects.get(id=1)
    if request.method == 'POST':
        order = Order.objects.create(customer=request.user)
        for item in cart:
            OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            product_price=item['price'],
                                            product_count=item['product_count'],
                                            product_total=Decimal(item['product_count']) * Decimal(item['price']))
        # order.customer = request.user
        # order.save()
        cart.clear()
        return render(request, 'order_success.html', {'order': order,'logo': logo})
    return render(request, 'checkout.html', {'cart': cart,'logo': logo})

merchant = ""
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
def to_bank(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    amount = 0
    order_items = OrderItem.objects.filter(order=order)
    for item in order_items:
        amount += item.product_total
    callbackUrl = 'https://rokhaam.com/store/callback/'
    mobile = ''
    email = ''
    description = 'Test'
    result = client.service.PaymentRequest(merchant, amount, description, email, mobile, callbackUrl)

    if result.Status == 100 and len(result.Authority) == 36:
        Invoice.objects.create(order=order,
                                      authority=result.Authority)
        return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
    else:
        return HttpResponse('Error code ' + str(result.Status))

def callback(request):
    logo = imagesite.objects.get(id=1)
    if request.GET.get('Status') == 'OK':
        authority = request.GET.get('Authority')
        invoice = get_object_or_404(Invoice, authority=authority)
        amount = 0
        order = invoice.order
        order_items = OrderItem.objects.filter(order=order)
        for item in order_items:
            amount += item.product_total
        result = client.service.PaymentVerification(merchant, authority, amount)
        if result.Status == 100:
            Transaction.objects.create(user=request.user, invoice=invoice, amount=amount, status='completed')
            for item in order_items:
                UserProduct.objects.create(order=item.order, product=item.product, user=request.user )
            return render(request, 'call_back.html', {'invoice': invoice,'logo': logo})
        else:
            return HttpResponse('error ' + str(result.Status))
    else:
        return HttpResponse('error ')
        
