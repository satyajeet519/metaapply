from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book
    author = models.CharField(max_length=100)  # Author of the book
    publish_date = models.DateField()  # Publish date of the book
    isbn = models.CharField(max_length=13, unique=True)  # ISBN number (unique)

    def __str__(self):
        return self.title  # Display title when we print the object
