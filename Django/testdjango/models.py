from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, default=None)
    body = models.TextField(max_length=1024)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
