from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default = "", blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    notify = models.EmailField(max_length=255, default = "", blank=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Task)
def send_email_to_interested_party(sender, instance, created, **kwargs):
    if instance.complete:
        send_mail(
            'Subject here',
            'Here is the message'
            'from@example.com'
            [instance.notify, ],
            fail_silently=False,
        )