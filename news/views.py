from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

def tabularNews(request):
    news = News.objects.all().order_by('-create_date')
    return render(request, 'news/tabular_list.html', {'news': news})

class NewsLV(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 6


