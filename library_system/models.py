

from django.db import models
class Category (models.Model):
    name=models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    category=models.TextField
    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

