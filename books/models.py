from django.db import models

# Create your models here.

class Book(models.Model):
    tittle = models.CharField(max_length=250)
    subtittle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13)
    
    def __str__(self):
        return self.tittle