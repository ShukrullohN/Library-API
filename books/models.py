from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    content = models.TextField()
    pages = models.IntegerField()
    in_stock = models.BooleanField(default=False)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
