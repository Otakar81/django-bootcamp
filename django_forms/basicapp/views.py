from django.shortcuts import render
from . import forms
from .models import User

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation success!!')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})


def form_model_view(request):
    form = forms.MyModelForm()

    if request.method == 'POST':
        form = forms.MyModelForm(request.POST)

        if form.is_valid():
            print('Saving data!!')
            form.save()

    # Recupero gli utenti inseriti e confeziono il dizionario
    users = User.objects.order_by('last_name')
    my_dictonary = {'form': form, 'users': users}

    return render(request, 'basicapp/form_model_page.html', my_dictonary)
