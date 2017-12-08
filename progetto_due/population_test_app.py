# Script per popolare il DB con dati fake di prova
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'progetto_due.settings')

import django
django.setup()

# Fake population script
import random
from test_app.models import AccessRecord, Topic, Webpage, User
from faker import Faker

# Creo l'oggetto faker generator
fakegenerator = Faker()

# E la lista di topic da cui pescare in maniera random
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# Creo la funzione di servizio per la creazione di un nuovo topic
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()

    return t

# Creo la funzione che si occupa effettivamente del popolamento del DB
def populate(N = 5):

    for entry in range(N):

        # Recupero il topic per la nuova entry
        top = add_topic()

        # Creo i dati fake
        fake_url = fakegenerator.url()
        fake_date = fakegenerator.date()
        fake_name = fakegenerator.company()

        # Creo la web page
        webpage = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # Creo il fake access record per la pagina
        acc_rec = AccessRecord.objects.get_or_create(name = webpage, date = fake_date)[0]


def populate_user(N = 5):

    for entry in range(N):

        fake_fname = fakegenerator.first_name()
        fake_lname = fakegenerator.last_name()
        fake_email = fakegenerator.email()

        User.objects.get_or_create(first_name = fake_fname, last_name = fake_lname, email = fake_email)


if __name__ == '__main__':
    print('Populating script...')
    #populate(20)
    populate_user(10)
    print('Population complete!')