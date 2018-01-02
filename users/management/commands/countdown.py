from users.models import Member
Member.objects.all.update(submissions_today=0)