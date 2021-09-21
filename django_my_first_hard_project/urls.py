from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('main.urls')),
  path('news/', include('news.urls')),
  path('library/', include('library.urls')),
  path('log_in/', include('log_in.urls')),
  path('admin/', admin.site.urls),
  path('ckeditor/', include('ckeditor_uploader.urls')),
  path('captcha/', include('captcha.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
