from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('category/<int:category_id>/', get_category),
]
