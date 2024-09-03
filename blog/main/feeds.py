# feeds.py
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Blog

class LatestPostsFeed(Feed):
	title = "Latest Blog Posts"
	link = "/blogs/"  # Main blog list URL
	description = "Updates on the latest blog posts."

	def items(self):
		return Blog.objects.order_by('-created_at')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.content[:200]  # First 200 characters as description

	def item_link(self, item):
		return reverse('blog_post', args=[item.created_at.year, item.created_at.month, item.created_at.day, item.slug])
