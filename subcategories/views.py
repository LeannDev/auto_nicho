from django.views import View
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

class SubCategory1View(View):

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

        return render(request, 'subcategory_1.html', context)
    
class SubCategory2View(View):

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

        return render(request, 'subcategory_2.html', context)
    
# Category #2
class SubCategory2IView(View):

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

        return render(request, 'subcategory_2I.html', context)
    
class SubCategory2IIView(View):

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

        return render(request, 'subcategory_2II.html', context)