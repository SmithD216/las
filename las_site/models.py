from django.db import models

# Create your models here.
class Entry(models.Model):
    """A submitted drawing entry."""
    image = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    blurb = models.CharField(max_length=200)

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

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text