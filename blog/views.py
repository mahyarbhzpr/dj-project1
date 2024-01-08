from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from core.models import imagesite, contentsite
# Create your views here.
from .forms import CommentForm
from customize.models import *
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def BlogsView(request):
    logo = imagesite.objects.get(id=1)
    banner = imagesite.objects.get(id=16)
    content = contentsite.objects.get(id=16)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    post = Post.objects.all()
    template_name = 'blog.html'
    context = {'blogs': post,'css': css, 'js': js, 'banner': banner,'logo': logo , 'content': content}
    return render(request, 'blog.html', context)
    
@csrf_exempt 
def BlogDetailView(request, slug):
    logo = imagesite.objects.get(id=1)
    css = CustomCss.objects.all()
    js = Custom_Js.objects.all()
    blog = get_object_or_404(Post, slug=slug)
    categorys = Category.objects.filter(categories=blog)
    tag = Tag.objects.filter(tag=blog)
    kw = keyword.objects.filter(keyword=blog)
    recents = Post.objects.all().order_by('date_created')[:4]
    comments = blogComment.objects.filter(blog=blog)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_phone = form.cleaned_data["phone"]
            new_description = form.cleaned_data["description"]

            new_comment = blogComment(blog=blog,name=new_name,phone=new_phone,description=new_description)
            new_comment.save()
            form = CommentForm(request.POST)
    context = {'blog': blog, 'cats': categorys, 'tags': tag, 'kw': kw, 'rec': recents, 'comment': comments,'css': css, 'js': js,'logo': logo}
    return render(request, 'blog-details.html', context)
    
def blog_tag(request, slug):
    logo = imagesite.objects.get(id=1)
    tag = get_object_or_404(Tag, slug=slug)
    blogs = Post.objects.filter(tags__slug=tag.slug)
    context = {'blogs': blogs,'logo': logo}
    return render(request, 'blog.html', context)
    
def blog_category(request, slug):
    logo = imagesite.objects.get(id=1)
    category = get_object_or_404(Category, slug=slug)
    blogs = Post.objects.filter(category__slug=category.slug)
    context = {'blogs': blogs,'logo': logo}
    return render(request, 'blog.html', context)
    
def Search(request):
    logo = imagesite.objects.get(id=1)
    if request.method == 'GET':
        q = request.GET.get('search')
    blogs = Post.objects.filter(title__contains=q, is_live=1)
    return render(request, 'blog.html', context={'blogs': blogs,'logo': logo})