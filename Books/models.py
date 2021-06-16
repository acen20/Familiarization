from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    book_name = models.CharField(max_length = 200)
    date = models.DateTimeField()

    def __str__(self):
        return self.book_name
