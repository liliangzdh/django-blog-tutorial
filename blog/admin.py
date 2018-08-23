
from django.contrib import admin
from .models import Category, Post, Tag
# Register your models here.


class Post_showAll(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'excerpt', 'category', 'pk', 'author']


class Tag_show(admin.ModelAdmin):
    list_display = ['name', "pk"]


admin.site.register(Category)
admin.site.register(Post, Post_showAll)
admin.site.register(Tag, Tag_show)

