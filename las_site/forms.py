from django import forms

from .models import Entry, Comment

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['image', 'blurb']
        labels = {'image':'Image url ', 'blurb':'Description '}
        widgets = {'blurb': forms.Textarea(attrs={'rows': 2, 'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
