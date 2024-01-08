from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, View, CreateView
from .form import *
from blog.models import Post

from django.shortcuts import get_object_or_404

# Create your views here.

def HomeView(request):
    logo = get_object_or_404(logo, id=1)
    team = Team.objects.all()
    portfolio = Portfolio.objects.all()
    service = Services.objects.all()
    customer = customer_comment.objects.all()
    faq = FAQ.objects.all()
    slider = Slider.objects.all()
    blog = Post.objects.all().order_by('date_created')[:3]
    context = {'teams': team, 'portfolios': portfolio, 'services': service, 'comments': customer, 'faq': faq, 'slide':slider, 'blg':blog, 'logo':logo}
    return render(request, 'home.html', context)


class portfoliodetail(DetailView):
    model = Portfolio
    template_name = "portfolio.html"
    context_object_name = 'portfolio'


def ContactView(request):
    logo = get_object_or_404(logo, id=1)
    # create object of form
    form = contacts(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context = {'form':form, 'logo':logo}
    return render(request, "contacts.html", context)