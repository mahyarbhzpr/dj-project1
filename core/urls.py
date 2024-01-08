from django.urls import path
from .views import *
app_name = 'core'
urlpatterns = [
    path('', HomeView, name='home'),
    path('contacts/', ContactView, name='contacts'),
    path('dashboard/', dashboard, name='dashboard'),
    path('about-us/', aboutus, name='aboutus'),
    path('faq/', faqview, name='faqview'),
    path('services/', servicesview, name='services'),
    path('project/', projects, name='projects'),
    path('projectg/', projectsg, name='projectsg'),
    path('gallery/', gallery_list, name='gallery'),
    path('project/<slug>/', portfoliodetail, name='project'),
    path('projectg/<slug>/', portfoliogdetail, name='projectg'),
    path('search/', Search, name='search'),
    path('media/', medias, name='media'),
    path('footer/', footer, name='media'),
]
