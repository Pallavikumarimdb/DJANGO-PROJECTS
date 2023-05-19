from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    # To see the name of sender in database entry
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    # To see the name of sender in database entry
    def __str__(self):
        return self.title