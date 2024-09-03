from django.db import models

from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils import timezone




from froala_editor.fields import FroalaField
  


class Blog(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    content = FroalaField()
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = TaggableManager() 
    thumbnail_image = models.ImageField(upload_to='thumbnails/',null=True, blank=True)
    content_type = models.CharField(max_length=100,null=True,blank=True)
    alt = models.CharField(max_length=100,null=True,blank=True)
    thumbnail_link = models.URLField(null=True, blank=True)  # Corrected `thumbline_link` to `thumbnail_link`
    meta = models.TextField(null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True, max_length=500)  # Corrected `uqnic` to `unique`
    
    def save(self, *args, **kwargs):  # Fixed typo `srlf` to `self`
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    