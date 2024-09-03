from django.urls import path,include
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap
from .feeds import LatestPostsFeed

sitemaps = {
	'blogs': BlogSitemap,
}



urlpatterns = [
    path('robots.txt', robots_txt, name='robots_txt'),
    path('rss/', LatestPostsFeed(), name='rss_feed'),
    
    path("",blog_list,name='blog_list'),
    path('blog/<int:year>/', blog_list, name='blog_by_year'),
    path('blog/<int:year>/<int:month>/', blog_list, name='blog_by_month'),
    path('blog/<int:year>/<int:month>/<int:day>/', blog_list, name='blog_by_day'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:title>/', blog_post, name='blog_post'),

    
    path('blog_list_json/', blog_list_json, name='blog_list_json'),
    path("search/", SearchResults ,name="search_results"),
    path('tag/<slug:tag_slug>/', TaggedBlogsView.as_view(), name='tagged_blogs'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
   
]
