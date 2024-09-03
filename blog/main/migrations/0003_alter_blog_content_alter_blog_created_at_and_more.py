# Generated by Django 5.1 on 2024-09-01 09:51

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_likedip_delete_articless_blog_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
