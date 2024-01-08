from django.shortcuts import render, get_object_or_404
from .models import *
from .form import *
from blog.models import Post
from customuser.models import MyUser
from customize.models import *
from shop.models import *
from prices.models import PriceMeterForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.translation import activate


def header(request, id):
    logo = imagesite.objects.get(id=1)
    return render(request, 'header.html', context={'logo': logo})
def footer(request):
    logo = imagesite.objects.get(id=1)
    return render(request, 'footer.html', context={'logo': logo})

@login_required
def dashboard(request):
    logo = imagesite.objects.get(id=1)
    form = dashboarduser(data=request.POST, instance=request.user)
    pricemeter = PriceMeterForm.objects.filter(user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    user_product = UserProduct.objects.filter(user=request.user)
    return render(request, 'dashboard.html', context={'css': css, 'js': js,'form': form,'logo': logo, 'productuser': user_product, "pricemeter": pricemeter})

def HomeView(request):
    content1 = contentsite.objects.get(id=1)
    content2 = contentsite.objects.get(id=2)
    content3 = contentsite.objects.get(id=3)
    content4 = contentsite.objects.get(id=4)

    background = imagesite.objects.get(id=2)
    section = imagesite.objects.get(id=3)
    contactimg = imagesite.objects.get(id=4)
    logo = imagesite.objects.get(id=1)
    cm = customer_comment.objects.all()
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    
    slider = Slider.objects.all()
    services = Services.objects.all()
    context = {'slide':slider,'css': css, 'js': js, 'cm':cm,'services': services,'logo': logo, 'background': background, 'section': section, 'contact': contactimg, 'content1': content1,'content2': content2,'content3': content3,'content4': content4}
    return render(request, 'home.html', context)

def faqview(request):
    logo = imagesite.objects.get(id=1)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    faq = FAQ.objects.all()
    return render(request, 'faq.html', context={'faq': faq,'css': css, 'js': js,'logo': logo})

def aboutus(request):
    logo = imagesite.objects.get(id=1)
    content1 = contentsite.objects.get(id=9)
    content2 = contentsite.objects.get(id=10)
    content3 = contentsite.objects.get(id=11)
    content4 = contentsite.objects.get(id=12)
    content5 = contentsite.objects.get(id=13)
    banner = imagesite.objects.get(id=12)
    aboutimg = imagesite.objects.get(id=14)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    team = Team.objects.all()
    context={'teams': team,'css': css, 'js': js,'logo': logo, 'banner': banner, 'about': aboutimg, 'content1': content1,'content2': content2,'content3': content3,'content4': content4, 'content5': content5}
    return render(request, 'about-us.html', context)

def servicesview(request):
    logo = imagesite.objects.get(id=1)
    content = contentsite.objects.get(id=5)
    background = imagesite.objects.get(id=5)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    services = Services.objects.all()
    return render(request, 'services.html', context={'services': services,'css': css, 'js': js,'logo': logo, 'background': background, 'content': content})

def projects(request):
    logo = imagesite.objects.get(id=1)
    content1 = contentsite.objects.get(id=7)
    content2 = contentsite.objects.get(id=8)
    leftimg = imagesite.objects.get(id=6)
    centerimg = imagesite.objects.get(id=7)
    rightimg = imagesite.objects.get(id=8)
    sectionimg = imagesite.objects.get(id=10)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    category = Category.objects.all()
    portfolio = Portfolio_architecture.objects.all()
    context = {'category': category, 'portfolio': portfolio,'css': css, 'js': js,'logo': logo, 'leftimg': leftimg, 'centerimg': centerimg, 'rightimg': rightimg, 'sectionimg': sectionimg, 'content1': content1, 'content2': content2}
    return render(request, 'project.html', context)
def gallery_list(request):
    logo = imagesite.objects.get(id=1)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    category = Category.objects.all()
    gallerys = gallery.objects.all()
    context = {'category': category, 'gallery': gallerys,'css': css, 'js': js,'logo': logo}
    return render(request, 'gallery.html', context)
def portfoliodetail(request, slug):
    logo = imagesite.objects.get(id=1)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    portfolio = get_object_or_404(Portfolio_architecture, slug=slug)
    context = {'portfolio':portfolio,'css': css, 'js': js,'logo': logo}
    return render(request, "portfolio.html", context)
def ContactView(request):
    logo = imagesite.objects.get(id=1)
    content1 = contentsite.objects.get(id=14)
    content2 = contentsite.objects.get(id=15)
    contactimg = imagesite.objects.get(id=4)
    rightimg = imagesite.objects.get(id=15)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    form = contacts(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form,'css': css, 'js': js,'logo': logo, 'contact': contactimg, 'rightimg': rightimg, 'content1': content1, 'content2': content2}
    return render(request, "contacts.html", context)

def projectsg(request):
    logo = imagesite.objects.get(id=1)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    category = Category.objects.all()
    portfolio = Portfolio_Graphic.objects.all()
    context = {'category': category, 'portfolio': portfolio,'css': css, 'js': js,'logo': logo}
    return render(request, 'projectg.html', context)
    
def portfoliogdetail(request, slug):
    logo = imagesite.objects.get(id=1)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    portfolio = get_object_or_404(Portfolio_Graphic, slug=slug)
    context = {'portfolio':portfolio,'css': css, 'js': js,'logo': logo}
    return render(request, "portfoliog.html", context)
    
def Search(request):
    logo = imagesite.objects.get(id=1)
    if request.method == 'GET':
        q = request.GET.get('search')
    blogs = Post.objects.filter(title__contains=q)
    return render(request, 'blog.html', context={'blogs': blogs,'logo': logo})
    
@login_required
def medias(request):
    if request.user.is_superuser:
        medias = media.objects.all()
        return render(request, 'media.html', context={'media': medias})
    else:
        return redirect("/")
        
def change_lang(request):
	activate(request.GET.get('lang'))
	return redirect(request.GET.get('next'))