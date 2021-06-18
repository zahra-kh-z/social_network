from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField('Book name', max_length=100)
    book_author = models.CharField('book author', max_length=100)
    publication_year = models.CharField('year of book publication', max_length=4)
    registration_time = models.DateTimeField('book registration time', auto_now_add=True)
    update_time = models.DateTimeField('update time Book information')
    username_register = models.CharField('username that registered this book', max_length=50, unique=True)

    def __str__(self):
        return f'{self.username_register} registered at {self.registration_time} the {self.book_name}'
