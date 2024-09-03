from django.shortcuts import render, get_object_or_404
from .models import  Blog
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.urls import reverse
from django.db.models import Q
from django.views.generic import ListView
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from taggit.models import Tag

from django.shortcuts import render, get_object_or_404
from .models import  Blog
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.urls import reverse
from django.db.models import Q
from django.views.generic import ListView
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from taggit.models import Tag


# views.py
from django.http import HttpResponse
from django.template import loader

def robots_txt(request):
	template = loader.get_template('robots.txt')
	return HttpResponse(template.render(), content_type='text/plain')
 

def get_top_tags(limit=10):
    # Annotate tags with the count of their usage and order by count
    top_tags = Tag.objects.annotate(num_times=Count('taggit_taggeditem_items')).order_by('-num_times')[:limit]
    return top_tags



    

class TaggedBlogsView(ListView):
    template_name = 'tagged_blogs.html'
    
    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return Blog.objects.filter(category__slug=tag_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_slug']
        return context


def SearchResults(request):
	query = request.GET.get("q", "").strip()  # Retrieve and strip whitespace from the query


	queryset = Blog.objects.filter(
		Q(title__icontains=query) | Q(category__name__icontains=query)
	).distinct()

	results = []
	for blog in queryset:
		matched_title = query.lower() in blog.title.lower()
		matched_category = any(query.lower() in tag.name.lower() for tag in blog.category.all())

		result = {
			'title': blog.title,
			'categories': [tag.name for tag in blog.category.all()],
			'matched_title': matched_title,
			'matched_category': matched_category,
			'year': blog.created_at.year,   # Add this
			'month': blog.created_at.month, # Add this
			'day': blog.created_at.day,     # Add this
			'slug': blog.slug               # Add this if using slug in the URL
		}
		results.append(result)

	# For debugging or logging purposes (optional)
	for result in results:
		print(f"Title: {result['title']}")
		if result['matched_title']:
			print("Match found in Title")
		if result['matched_category']:
			print(f"Match found in Category: {result['categories']}")

	return render(request, 'search_results.html', {'results': results, 'query': query})

def blog_list(request):
    top_tags = get_top_tags()
    return render(request, 'blog_list.html', {'top_tags': top_tags})




def blog_list_json(request, year=None, month=None, day=None):
    filters = {}
    if year:
        filters['created_at__year'] = year
    if month:
        filters['created_at__month'] = month
    if day:
        filters['created_at__day'] = day

    page_number = int(request.GET.get('page', 1))
    blog_list = Blog.objects.filter(**filters).order_by('-created_at')
    paginator = Paginator(blog_list, 6)
    page_obj = paginator.get_page(page_number)

    blogs = []
    for blog in page_obj:
        blogs.append({
            'title': blog.title,
            'created_at': blog.created_at.strftime('%Y-%m-%d'),
            'category': blog.category,  # Make sure this is serializable
            'thumbnail_image': blog.thumbnail_image.url if blog.thumbnail_image else None,
            'thumbnail_link': blog.thumbnail_link,
            'truncated_content': Truncator(strip_tags(blog.content)).words(10, truncate='...'),
            'category': list(blog.category.names()),  # Convert _TaggableManager to a list
            'url': reverse('blog_post', args=[blog.created_at.year, blog.created_at.month, blog.created_at.day, blog.slug])
        })

    has_next = page_obj.has_next()

    return JsonResponse({'blogs': blogs, 'has_next': has_next})

def blog_post(request, year, month, day, title):
    blog = get_object_or_404(
        Blog,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
        slug=title
    )
    return render(request, 'blog_detail.html', {'blog': blog})


