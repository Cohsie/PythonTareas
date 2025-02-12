from django.contrib import admin

from library.models import Author
from library.models import Book
from library.models import Publisher
from library.models import Loan

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Loan)

# Register your models here.
