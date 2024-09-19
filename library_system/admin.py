from django.contrib import admin
from.models import Book



class LibraryAdmin(admin.ModelAdmin):
    list_display= ("title","author","description", "borrowed","category")
admin.site.register(Book, LibraryAdmin)

