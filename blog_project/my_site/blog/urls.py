from django.conf.urls import url
from blog import views


# IMPORT TAGGING
app_name = 'blog'

urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name = 'about'),
]