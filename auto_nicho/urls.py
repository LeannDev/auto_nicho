from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import HomeView, AboutUsView, CookiesView, LegalView, PrivacyView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', include('categories.urls')),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('cookies/', CookiesView.as_view(), name='cookies'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('admin/', admin.site.urls),
]

# Static files route
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
