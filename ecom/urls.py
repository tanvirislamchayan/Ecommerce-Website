from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# <img src="{% static 'images/example.jpg' %}" alt="Example Image">

# <img src="{{ instance.image.url }}" alt="Image">
