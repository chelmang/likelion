from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Tag, Blog, Post, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Comment)


