from django.views import View
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

class HomeView(View):

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

        return render(request, 'home.html', context)
    
class AboutUsView(View):

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

        return render(request, 'about_us.html', context)
    
class CookiesView(View):

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

        return render(request, 'politics/cookies.html', context)
    
class LegalView(View):

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

        return render(request, 'politics/legal.html', context)
    
class PrivacyView(View):

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

        return render(request, 'politics/privacy.html', context)