# from django.core.mail import send_mail
from django.db import models

# Create your models here.

def send_an_email():
    print("Sending an email")


class Task(models.Model):
    objects = None
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="", blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    notify = models.EmailField(max_length=255, default="", blank=True)
    category = models.CharField(max_length=45, default="", choices=(('HOMEWORK', 'HOMEWORK'), ('GROUPWORK', 'GROUPWORK'), ('WORKSTUDY', 'WORKSTUDY')))
    priority = models.CharField(max_length=45, default="", choices=(('PRIORITY', 'PRIORITY'), ('NON-PRIORITY', 'NON-PRIORITY')))
    task_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.complete and self.notify:
            send_an_email()