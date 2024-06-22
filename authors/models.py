from django.db import models

class AuthorModel(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55)
    email = models.CharField(max_length = 55)
    Phone_number = models.CharField(max_length = 14)
    age = models.IntegerField(max_length = 55)
    firsl_name = models.CharField(max_length = 55)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'