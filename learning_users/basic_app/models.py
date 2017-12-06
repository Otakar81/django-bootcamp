from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Si tratta di una estensione del model User standard. Setto la relazione OneToOneField
    user = models.OneToOneField(User)

    # Aggiungo degli attributi
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username
