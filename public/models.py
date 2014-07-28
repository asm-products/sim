from django.db import models

# Create your models here.


class InviteRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField()
    token = models.CharField(max_length=128)
    verified = models.BooleanField()
    validated = models.BooleanField()
