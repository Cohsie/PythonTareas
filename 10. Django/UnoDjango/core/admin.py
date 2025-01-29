from django.contrib import admin
from core.models import Author
from core.models import Book
# Register your models here.

admin.site.register(Author)

admin.site.register(Book)