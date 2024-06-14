from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
try:
    from web import views
except ImportError as e:
    import traceback
    print(traceback.format_exc())
    raise e

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('contacts/', views.contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
