"""Defines URL patterns for las_site."""

from django.conf.urls import url

from . import views

app_name = 'las_site'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
]