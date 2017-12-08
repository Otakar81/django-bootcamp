from django.db import models

# Create your models here.
class Titolo(models.Model):
    descrizione = models.CharField(max_length=50)

    def __str__(self):
        return self.descrizione


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)

    titolo = models.ForeignKey(Titolo)

    def __str__(self):
        return self.last_name + ' ' + self.first_name[0] + '.'
