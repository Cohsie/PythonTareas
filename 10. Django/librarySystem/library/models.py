from django.db import models
import datetime

class Author(models.Model):
    first_name = models.CharField(verbose_name='Nombre', max_length=100, default='')
    last_name = models.CharField(verbose_name='Apellido', max_length=150, default='')
    age = models.PositiveSmallIntegerField(verbose_name='Edad')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, default='')
    address = models.CharField(verbose_name='Dirección', max_length=140, default='')
    city = models.CharField(verbose_name='Ciudad', max_length=100, default='')
    state_province = models.CharField(verbose_name='Provincia', max_length=100, default='')
    country = models.CharField(verbose_name='País', max_length=100, default='')
    website = models.CharField(verbose_name='Sitio web', max_length=150, default='')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100, default='')
    authors = models.ManyToManyField(Author, verbose_name='Autores')  # Cambiado a ManyToManyField
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='Editorial')  # Relación correcta
    publication_date = models.DateField(verbose_name='Fecha de publicación', default=datetime.date.today)

    def __str__(self):
        return self.title


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Libro')  # Relación con Book
    borrower = models.CharField(verbose_name='Prestatario', max_length=100, default='')
    loan_date = models.DateField(verbose_name='Fecha de préstamo', default=datetime.date.today)
    return_date = models.DateField(verbose_name='Fecha de devolución', null=True, blank=True)  # Permitir fechas nulas

    def __str__(self):
        return f'{self.borrower} - {self.book}'