from django.urls import path, include

from .views import Category1View, Category2View

urlpatterns = [
    path('category-1/', Category1View.as_view(), name='category-1'),
    path('category-1/', include('subcategories.urls')),
    path('category-2/', Category2View.as_view(), name='category-2'),
    path('category-2/', include('subcategories.urls2')),
]