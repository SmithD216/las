from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Entry, Comment
from .forms import EntryForm, CommentForm

def index(request):
    """The home page and submission form for las."""
    entries = Entry.objects.order_by('-date_added')

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('las_site:index'))

    context = {'entries': entries, 'form': form}
    return render(request, 'las_site/index.html', context)

@login_required
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
            new_comment.owner = request.user
            new_comment.entry = entry
            new_comment.save()
            return HttpResponseRedirect(reverse('las_site:entry', args=[entry_id]))

    context = {'entry':entry, 'comments':comments, 'form':form}
    return render(request, 'las_site/entry.html', context)

@login_required
def edit_comment(request, comment_id):
    """Edit an existing comment."""
    comment = Comment.objects.get(id=comment_id)
    entry = comment.entry

    if comment.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('las_site:entry', args=[entry.id]))
    
    context = {'entry':entry, 'comment': comment, 'form': form}
    return render(request, 'las_site/edit_comment.html', context)