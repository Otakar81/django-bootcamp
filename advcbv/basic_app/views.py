from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from . import models

# Create your views here.

# View classica vista fino ad ora
def index(request):
    return render(request, 'index.html')

# Class based Views

# Classe base, con una semplice HttpResponse
class CBView(View):
    def get(self, request):
        return HttpResponse("Sono in una Class Based View!")

# Classe che implementa un template.html
class IndexView(TemplateView):
    template_name = 'index.html'

    # Per passare info tramite dizionario al template
    # Il parametro preceduto da ** sta proprio ad indicare un dizionario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dato_esempio'] = "BASIC INJECTION!"

        return context

# CBV che implementa la GenericView pensata per stampare una lista di elementi di un modello
class SchoolListView(ListView):

    # La classe ListView crea "gratis" un context di ritorno il cui nome è il nome della classe del modello
    # seguita da _list, tutto minuscolo
    # In questo caso, senza far nulla, la lista di oggetti sarà restituita alla view col nome "school_list"
    # Possiamo cambiare il nome di questo context facendo override della proprietà che segue
    context_object_name = 'schools' # Nome "personalizzato" del context restituito nella view

    model = models.School

# CBV che implementa la stampa del dettaglio di un elemento del modello
class SchoolDetailView(DetailView):

    # Il nome di default del context restituito dalla DetailView è il nome del modello in lowecase
    # In questo caso avremmo "school"
    # Personalizziamo
    context_object_name = 'school_detail'

    model = models.School
    template_name = 'basic_app/school_detail.html'

# CRUD: Create
class SchoolCreateView(CreateView):

    # Di default, la CreateView si aspetta l'esistenza di un template di nome MODELNAME_form.html
    # In questo caso: school_form.html

    # In una CreateView DEVO specificare quali campi possono essere inseriti
    fields = ('name', 'principal', 'location')

    model = models.School


# Update: le caratteristiche sono molto simili a quelle della create
class SchoolUpdateView(UpdateView):

    # Ipotizziamo che nome e principal si possano modigicare, mentre la location di una scuola difficilmente cambia
    fields = ('name', 'principal')

    model = models.School

# Delete
class SchoolDeleteView(DeleteView):

    # Il nome di default del context restituito dalla DetailView è il nome del modello in lowecase
    # In questo caso avremmo "school"

    model = models.School
    success_url = reverse_lazy("basic_app:list")