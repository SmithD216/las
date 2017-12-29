from django.shortcuts import render

from .models import Entry

def index(request):
    """The home page for las."""
    entries = Entry.objects.order_by('date_added')
    context = {'entries': entries}
    return render(request, 'las_site/index.html', context)

def entry(request, entry_id):
    """Show a single entry and all its comments."""
    entry = Entry.objects.get(id=entry_id)
    comments = entry.comment_set.order_by('-date_added')
    context = {'entry':entry, 'comments':comments}
    return render(request, 'las_site/entry.html', context)