from users.models import Member
u = Member.objects.all()
u.update(submissions_today=0)
u.save()
