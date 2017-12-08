# File degli url della singola applicazione
# Chiamato dal file "urls" del progetto tramite il metodo "include"
from django.conf.urls import url
from test_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/', views.help, name='help'),
    url(r'^dambo/', views.dambo, name='dambo'),
    url(r'^accr/', views.access_records, name='accr'),
    url(r'^users/', views.users, name='users'),
]