from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse

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
    model = models.School

# CBV che implementa la stampa del dettaglio di un elemento del modello
class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'