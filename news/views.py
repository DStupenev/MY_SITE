from django.shortcuts import render

from .models import News


def news_home(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей.'
    }
    return render(request, template_name='news/news_home.html', context=context )
