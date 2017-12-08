from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import AccessRecord, Topic, Webpage, User


# Create your views here.

# View base: semplice invio di una stringa tramite HttpResponse
#def index(request):
#    return HttpResponse('<em>Hola Amigo!</em>')

# View base: uso di un templates html con un dizionario associato per valorizzare delle semplici variabili
def index(request):
    my_dictonary = {'insert_me': 'Valore proveniente dal dizionario'}

    return render(request, 'test_app/index.html', context=my_dictonary)

def help(request):
    my_dictonary = {
        'te_name': 'gentile Ospite',
        'me_name': 'Django',
    }

    return render(request, 'test_app/help.html', context=my_dictonary)

def dambo(request):
    my_dictonary = {}

    return render(request, 'test_app/dambo.html', context=my_dictonary)

# Integrazione con i modelli per stampa degli oggetti memorizzati nel DB
def access_records(request):
    lista_ar = AccessRecord.objects.order_by('date')

    my_dictionary = {'access_records': lista_ar}

    return render(request, 'test_app/accr.html', context = my_dictionary)

def users(request):
    lista_usr = User.objects.order_by('last_name')

    my_dictionary = {'users': lista_usr}

    return render(request, 'test_app/users.html', context = my_dictionary)