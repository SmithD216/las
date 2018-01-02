from django.core.management.base import BaseCommand, CommandError
from users.models import Member

class Command(BaseCommand):
    help = "The countdown script that resets the daily submission counter of the users."
    def handle(self, *args, **options):
        Member.objects.update(submissions_today=0)
        self.stdout.write("Daily submissions have been successfuly reset to zero.")