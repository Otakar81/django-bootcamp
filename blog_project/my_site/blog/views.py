from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)


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
        return Post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model = Post

# Si tratta di una view che richiede autenticazione.
# Le faccio ereditare anche i metodi di LoginRequiredMixin, che si occuperà di gestire la cosa
class CreatePostView(LoginRequiredMixin, CreateView):

    # Da LoginRequiredMixin
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    # Da create view
    model = Post
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # Da LoginRequiredMixin
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    # Da create view
    model = Post
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class DraftListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    # Occorre personalizzarlo, altrimenti andrebbe di default su "NOME-MODEL_list.html"
    template_name = 'post_draft_list.html'

    model = Post


    # Personalizzo la query effettuata per estrarre i dati da mostrare nella lista
    def get_queryset(self):
        # Il filter ha come argomento una stringa nella forma: nomecampo__fieldlookup
        # Nello specifico, chiediamo i post che abbiano "published date" che sia
        # lte (less than or equal to) la data attuale
        # Ordinati per "published date", ascendente (il meno davanti al campo)
        return Post.objects.filter(publish_date__isnull=True).order_by('create_date')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish()

    redirect('blog:post_detail', pk = pk)

#
# Commenti
#
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if(request.method == 'POST'):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()

            return redirect('blog:post_detail', pk = post.pk)

    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()

    return redirect('blog:post_detail', pk = comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)

    post_pk = comment.post.pk

    comment.delete()

    return redirect('blog:post_detail', pk = post_pk)