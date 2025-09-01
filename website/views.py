from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def whatWeDo(request):
    return render(request, 'what-we-do.html')

def contactUs(request):
    return render(request, 'contact-us.html')

def newsEvent(request):
    return render(request, 'news-event.html')

def newsDetail(request, slug):
    return render(request, 'news-detail.html')

def publication(request):
    return render(request, 'publication.html')

def gallery(request):
    return render(request, 'gallery.html')