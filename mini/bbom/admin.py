from django.contrib import admin
from .models import Post, Comment, Category, Menu, Univ, Summary

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Univ)
admin.site.register(Summary)