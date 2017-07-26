from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from main_app.models import Faculty
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    faculty = models.ForeignKey(Faculty, blank=True)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20)
    # needed for AbstractBaseUser model

    objects = UserManager() # manager for user - to-do

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    # список имен полей, которые будут запрашиваться при 
    # создании пользователя с помощью команды управления createsuperuser

    class Meta:
        verbose_name = "captain"
        verbose_name_plural = "captains"

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)