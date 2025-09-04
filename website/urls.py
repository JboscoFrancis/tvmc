

from website import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.aboutUs, name='about-us'),
    path('what-we-do', views.whatWeDo, name='what-we-do'),
    path('contact-us', views.contactUs, name='contact-us'),
    path('news-event', views.newsEvent, name='news-event'),
    path('news-detail/<slug:slug>', views.newsDetail, name='news-detail'),
    path('publication', views.publication, name='publication'),
    path('gallery', views.gallery, name='gallery'),
]