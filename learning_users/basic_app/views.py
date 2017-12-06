from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Login view
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("Ypu are logged in, Nice!!")

# Utilizzo il decorator "login_required", perchè non posso fare logout se non sono loggato
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            # Creo lo USER dalla form, e lo salvo su DB
            user = user_form.save()
            user.set_password(user.password) # Fa l'hash della password sulla base del settings.py
            user.save()

            # Salvo le info estensione
            profile = profile_form.save(commit = False) # Voglio essere sicuro di non avere collisioni con USER
            profile.user = user

            # Se c'è ò'immagine, la carico
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            # Registrazione completata con successo
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                            {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered': registered})



def user_login(request):

    if request.method == 'POST':
        # Recupero i valori dalla form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Effettua l'autenticazione
        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user) # Login vero e proprio nel portale
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'basic_app/login.html', {})
