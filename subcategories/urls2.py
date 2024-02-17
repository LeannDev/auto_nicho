from django.urls import path

from .views import SubCategory2IView, SubCategory2IIView

urlpatterns = [
    path('subcategory-1/', SubCategory2IView.as_view(), name='subcategory-2.1'),
    path('subcategory-2/', SubCategory2IIView.as_view(), name='subcategory-2.2'),
]