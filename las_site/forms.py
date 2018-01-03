from django import forms

from .models import Entry, Comment

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['image', 'blurb']
        labels = {'image':'Image url ', 'blurb':'Description '}
        widgets = {'blurb': forms.Textarea(attrs={'class' : 'desc-form','rows': 2, 'cols': 60})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
