from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Entry
from .forms import EntryForm, CommentForm

def index(request):
    """The home page and submission form for las."""
    entries = Entry.objects.order_by('date_added')

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('las_site:index'))

    context = {'entries': entries, 'form': form}
    return render(request, 'las_site/index.html', context)

def entry(request, entry_id):
    """Show a single entry and all its comments."""
    entry = Entry.objects.get(id=entry_id)
    comments = entry.comment_set.order_by('-date_added')

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.entry = entry
            new_comment.save()
            return HttpResponseRedirect(reverse('las_site:entry', args=[entry_id]))

    context = {'entry':entry, 'comments':comments, 'form':form}
    return render(request, 'las_site/entry.html', context)