from django import forms
from .models import Post, Comment

#
# Creo delle form legate ai modelli
#
class PostForm(forms.ModelForm):

    # Mappo form e model, e specifico quali campi mostrare
    class Meta():
        model = Post
        fields = {'authon', 'title', 'text'}

        #Posso associare ogni campo a delle classi CSS specifiche
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textInputClass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }




class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = {'authon', 'text'}

        # Posso associare ogni campo a delle classi CSS specifiche
        widgets = {
            'authon': forms.TextInput(attrs={'class': 'textInputClass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }