from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    """A submitted drawing entry."""
    image = models.URLField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    blurb = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return self.image

class Comment(models.Model):
    """A comment attached to an entry."""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text