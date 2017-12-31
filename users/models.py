from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    submissions_today = models.PositiveIntegerField(default=0)
    total_submissions = models.PositiveIntegerField(default=0)
