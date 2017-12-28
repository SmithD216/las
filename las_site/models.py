from django.db import models

# Create your models here.
class Entry(models.Model):
    """A submitted drawing entry."""
    image = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    blurb = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.image