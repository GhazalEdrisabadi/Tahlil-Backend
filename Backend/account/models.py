from django.contrib.auth.hashers import is_password_usable, get_hasher, identify_hasher
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Tailor(AbstractUser):
    Photo = models.ImageField(upload_to='userimage/')
    username = models.CharField(max_length=100, blank=False, unique=True)
    Confirm = models.CharField(max_length=100, blank=False, help_text='Confirm your password')
    Phone = models.CharField(max_length=15, blank=True)
    Address = models.TextField(max_length=300, blank=True)
    Evidence = models.ImageField(upload_to='madrakimage/', blank=True)
    WorkExprience = models.CharField(max_length=255, blank=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __unicode__(self):
        return self.username

    def str(self):
        return self.username

    def check_password(password, encoded, setter=None, preferred='default'):
        if password is None or not is_password_usable(encoded):
            return False

        preferred = get_hasher(preferred)
        try:
            hasher = identify_hasher(encoded)
        except ValueError:
            return False
