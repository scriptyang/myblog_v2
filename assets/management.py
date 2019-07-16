from django.db.models.signals import post_migrate
from django.contrib.auth.models import User


def init_user(sender, **kwargs):
    if sender.name == 'assets':
        if User.objects.all().count() == 0:
            User.objects.create_superuser(username='admin', password='admin', email='admin@myblog.com')


post_migrate.connect(init_user)