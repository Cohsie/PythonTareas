from django.db import models

# Create your models here.

class Author (models.Model):
    name=models.CharField(verbose_name='Nombre',
    max_length=100,
    default=''
    )
    last_name=models.CharField(verbose_name='Apellido',
    max_length=150,
    default='')
    age=models.PositiveSmallIntegerField (verbose_name='Edad',
    )

class Book (models.Model):
    title=models.CharField('Teo va a picar código', 
    max_length=255, 
    unique=True
    )
    cod=models.CharField('Código',
    max_length=15,
    unique=True
    )
    author=models.OneToOneField(Author,on_delete=models.CASCADE)

author=models.OneToOneField(Author,on_delete=models.SET_NULL,null=True)