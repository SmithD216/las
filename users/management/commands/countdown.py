from django.core.management.base import BaseCommand, CommandError
from users.models import Member

class Command(BaseCommand):
    Member.objects.update(submissions_today=0)