from django.shortcuts import render
from website.models import News
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    news_list = News.objects.all()[:5]
    top_priority = News.objects.order_by('priority')[:1]
    context = {
        'news': news_list,
        'top_priority': top_priority
    }
    return render(request, 'home.html', context)

def aboutUs(request):
    return render(request, 'about-us.html')

def whatWeDo(request):
    return render(request, 'what-we-do.html')

def contactUs(request):
    return render(request, 'contact-us.html')

def newsEvent(request):
    news_list = News.objects.all()[1:4]
    first_news = News.objects.all()[:1]
    all_news = News.objects.all()

    context = {
        'news': news_list,
        'latest': first_news,
        'all_news': all_news
    }
    return render(request, 'news-event.html', context)

def newsDetail(request, slug):
    news= get_object_or_404(News, slug=slug)
    return render(request, 'news-detail.html', {'news': news})

def publication(request):
    return render(request, 'publication.html')

def gallery(request):
    return render(request, 'gallery.html')