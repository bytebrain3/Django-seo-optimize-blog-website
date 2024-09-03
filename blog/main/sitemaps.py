# sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.8

	def items(self):
		return Blog.objects.all()

	def lastmod(self, obj):
		return obj.updated_at

	def location(self, obj):
		return f'/blog/{obj.slug}/'
		