from django.urls import path
from .views import *

urlpatterns = [
    path('', news_home, name='news_home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
]
