from django import forms
from .models import Post, Comment

#
# Creo delle form legate ai modelli
#
class PostForm(forms.ModelForm):

    # Mappo form e model, e specifico quali campi mostrare
    class Meta():
        model = Post
        fields = {'author', 'title', 'text'}

        #Posso associare ogni campo a delle classi CSS specifiche
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textInputClass form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent form-control'})
        }




class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = {'author', 'text'}

        # Posso associare ogni campo a delle classi CSS specifiche
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textInputClass form-control'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control'})
        }