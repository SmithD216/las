"""Defines URL patterns for las_site."""

from django.conf.urls import url

from . import views

app_name = 'las_site'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Individual entry page
    url(r'^entries/(?P<entry_id>\d+)/$', views.entry, name='entry'),
    # Comment edit page
    url(r'^edit_comment/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment')
]