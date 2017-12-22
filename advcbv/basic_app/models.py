from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

# Django crea "gratis" un campo numerico id, che usa come PK
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # Necessario per la CreateView. Deve sapere dove andare di default dopo l'inserimento
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk': self.pk})




class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()

    # Il "related name" è il nome dell'attributo con cui far riferimento a questa FK dalla classe School
    # L'elenco degli studenti della scuola, sarà ottenibile quindi come campo "students"
    school = models.ForeignKey(School, related_name='students')

    def __str__(self):
        return self.name