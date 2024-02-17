from django.views import View
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

class Category1View(View):

    def get(self, request):

        current_site = get_current_site(request) # get current site
        title = 'mi titulo'
        meta_description = 'mi meta description'
        social_title = title
        social_description = meta_description,
        image = '/image.webp'

        context = {
            'site': current_site,
            'title': title,
            'meta_description': meta_description,
            'social_title': social_title,
            'social_description': social_description,
            'image': image,
        }

        return render(request, 'category_1.html', context)
    
class Category2View(View):

    def get(self, request):

        current_site = get_current_site(request) # get current site
        title = 'mi titulo'
        meta_description = 'mi meta description'
        social_title = title
        social_description = meta_description,
        image = '/image.webp'

        context = {
            'site': current_site,
            'title': title,
            'meta_description': meta_description,
            'social_title': social_title,
            'social_description': social_description,
            'image': image,
        }

        return render(request, 'category_2.html', context)