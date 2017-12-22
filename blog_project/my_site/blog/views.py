from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView)
from blog.models import Post, Comment

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    # Personalizzo la query effettuata per estrarre i dati da mostrare nella lista
    def get_queryset(self):

        # Il filter ha come argomento una stringa nella forma: nomecampo__fieldlookup
        # Nello specifico, chiediamo i post che abbiano "published date" che sia
        # lte (less than or equal to) la data attuale
        # Ordinati per "published date", ascendente (il meno davanti al campo)
        return Post.objects.filter(published_date__lte = timezone.now().order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView):
    model = Post
