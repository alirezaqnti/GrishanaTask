from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from django.contrib.auth.hashers import make_password


@receiver(post_save, sender=User)
def user_create(sender, created, instance, *args, **kwargs):
    if created:
        PS = make_password(instance.password)
        User.objects.filter(pk=instance.pk).update(password=PS)
