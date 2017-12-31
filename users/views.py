from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from las_site.models import Entry
from .models import Member

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('las_site:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserCreationForm()
    else:
        # Process the completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect them to the home page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('las_site:index'))
    
    context = {'form':form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    member = Member.objects.get(user=user_id)

    entries = Entry.objects.filter(owner=user).order_by('-date_added')

    context = {'user':user, 'entries':entries, 'member':member}
    return render(request, 'users/profile.html', context)