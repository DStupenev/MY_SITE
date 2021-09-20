from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from news.views import get_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('library/', include('library.urls')),
    path('log_in/', include('log_in.urls')),
    # path('category/<int:category_id>/', get_category),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
