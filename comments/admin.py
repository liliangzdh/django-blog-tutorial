from django.contrib import admin
from .models import Comments
# Register your models here.


class Comments_show(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'text', 'create_time', 'post']


admin.site.register(Comments, Comments_show)
