
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('librarian/', admin.site.urls),
    path('', include('library.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
