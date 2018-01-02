from django.core.management.base import BaseCommand, CommandError
from users.models import Member

class Command(BaseCommand):

    def handle(self, *args, **options)
    Member.objects.update(submissions_today=0)

self.stdout.write("Daily submissions successfully reset.")
