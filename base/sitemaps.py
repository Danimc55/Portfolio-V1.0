from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'
    
    def items(self):
        return ['contact']

    def location(self, item):
        return reverse(item)
    
class MainSitemap(Sitemap):
    changefreq = "yearly"
    priority = 1
    protocol = 'https'
    
    def items(self):
        return ['page']

    def location(self, item):
        return reverse(item)