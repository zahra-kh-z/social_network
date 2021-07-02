from django.contrib import admin

# Register your models here.
# from book.models import Book
from .models import Book, Comment, Like

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Like)

# admin.site.register(Author)
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']

