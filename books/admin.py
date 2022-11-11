from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'authur', 'price', 'date_publication')


admin.site.register(Book, BookAdmin)