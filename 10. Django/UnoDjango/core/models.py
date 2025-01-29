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

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Book (models.Model):
    title=models.CharField('Nombre del libro', 
    max_length=255, 
    unique=True #Para no introducir dos libros con el mismo título
    )
    cod=models.CharField('Código',
    max_length=15,
    unique=True
    )
    author=models.OneToOneField(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

author=models.OneToOneField(Author,on_delete=models.SET_NULL,null=True)
#Indico que en el campo autor de un libro este se ponga null si dicho campo 
#se ha borrado

