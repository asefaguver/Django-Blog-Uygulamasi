from django.contrib import admin
from .models import Blog,Category


class BlogAdmin(admin.ModelAdmin):                  # blog tablosunda gösterilecek ve editlenecek içerikleri belirleyen metod
    list_display=("title","is_active","is_home")
    list_editable=("is_active","is_home")
    search_fields=("title","description")   # arama yapmak istenilen tablo içerikleri

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

