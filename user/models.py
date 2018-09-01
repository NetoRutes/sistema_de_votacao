from django.db import models
from django.conf import settings
from .signals import create_auth_token

# Create your models here.
models.signals.post_save.connect(create_auth_token, sender=settings.AUTH_USER_MODEL)