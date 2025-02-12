from django.db import models

# Create your models here.

class Author (models.Model):
    first_name=models.CharField(verbose_name='Nombre',
    max_length=100,
    default=''
    )
    last_name=models.CharField(verbose_name='Apellido',
    max_length=150,
    default=''
    )
    age=models.PositiveSmallIntegerField(verbose_name='Edad',
    )

class Publisher(models.Model):
    name=models.CharField(verbose_name='Nombre',
    max_length=100,
    default=''
    )
    address=models.CharField(verbose_name='Dirección',
    max_length=140,
    default=''
    )
    city=models.CharField(verbose_name='Ciudad',
    max_length=100,
    default=''
    )
    state_province=models.CharField(verbose_name='Provincia',
    max_length=100,
    default=''
    )
    country=models.CharField(verbose_name='País',
    max_length=100,
    default=''
    )
    website=models.CharField(verbose_name='Sitio web',
    max_length=150,
    default=''
    )

class Book(models.Model):
    title=models.CharField(verbose_name='Título',
    max_length=100,
    default=''
    )
    authors=models.CharField(verbose_name='Autores',
    max_length=100,
    default=''
    )
    publishers=models.CharField(verbose_name='Publishers',
    max_length=100,
    default=''
    )
    publication_date=models.DateField(verbose_name='Fecha',
    max_length=100,
    default=''
    )

class Loan(models.Model):
    book=models.CharField(verbose_name='Libro',
    max_length=100,
    default=''
    )
    borrower=models.CharField(verbose_name='Prestatario',
    max_length=100,
    default=''
    )
    loan_date=models.DateField(verbose_name='FechaLoan',
    max_length=100,
    default=''
    )
    return_date=models.DateField(verbose_name='FechaReturn',
    max_length=100,
    default=''
    )