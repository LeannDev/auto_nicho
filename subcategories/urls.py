from django.urls import path

from .views import SubCategory1View, SubCategory2View

urlpatterns = [
    path('subcategory-1/', SubCategory1View.as_view(), name='subcategory-1'),
    path('subcategory-2/', SubCategory2View.as_view(), name='subcategory-2'),
]