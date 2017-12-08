from django import forms
from django.core import validators


# Creo un validator personalizzato: il campo deve iniziare con una z
def check_for_z(value):
    if(value[0].lower() != 'z'):
        raise forms.ValidationError("Il nome deve iniziare con una Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again:")
    text = forms.CharField(widget=forms.Textarea)


    botcacher = forms.CharField(required=False, widget=forms.HiddenInput)

    botcacher_validator = forms.CharField(required=False, widget=forms.HiddenInput,
                                          validators=[validators.MaxLengthValidator(0)])


    # Il campo hidden "botcacher" è pensato per catturare l'intervento malevolo di un bot
    # Il campo è hidden, invisibile ad un essere umano, quindi in condizioni normali non sarà mai valorizzato
    # Un BOT invece, analizzando l'html, troverà il campo e proverà a valorizzarlo
    # In questo metodo, che si chiama "clean_NOME-CAMPO", verifico che il campo sia vuoto, altrimenti do errore
    # Posso ottenere lo stesso risultato usando il validator MaxLengthValidator (come per botcacher_validator)
    def clean_botcacher(self):
        botcacher = self.cleaned_data['botcacher']

        if len(botcacher) > 0:
            raise forms.ValidationError('GOTCHA BOT!!')


    # Il metodo "clean" riguarda l'intera form
    def clean(self):
        all_clean_data = super().clean() # Tutti i dati della form

        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError("Make sure emails match!")


# Form model: mappa una form di inserimento ad un modello
from .models import User

class MyModelForm(forms.ModelForm):
    # Mappo form e model
    class Meta:
        model = User
        fields = "__all__"
