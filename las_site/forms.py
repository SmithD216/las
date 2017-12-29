from django import forms

from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['image', 'blurb']
        labels = {'image':'Image url ', 'blurb':'Description '}