from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'published_at')
    list_filter = ('published_at', )
    search_fields = ('title', 'author_name', 'description')