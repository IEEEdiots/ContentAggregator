from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News

def home(request):
    return HttpResponse("This is the home page.")

def index(request):
    latest_news = News.objects.order_by('pub_date')[:5]
    context = {'latest_news': latest_news}
    return render(request, 'index.html', context)

def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'detail.html', {'news': news})