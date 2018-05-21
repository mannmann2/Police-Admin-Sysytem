#from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.db.models.signals import post_save


# Create your models here.


class TrafficFine(models.Model):
    full_name=models.CharField(max_length=120, blank=False, null=False)
    reciept_no=models.CharField(max_length=20, blank=False, null=False)
    offence=models.CharField(max_length=320, blank=False, null=False)
    amount=models.IntegerField(blank=False, null=False)
    status=models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return self.reciept_no


class FIR(models.Model):
    full_name=models.CharField(max_length=120, blank=False, null=False)
    FIR_No=models.CharField(max_length=20, blank=False, null=False)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    complaint=models.CharField(max_length=320, blank=False, null=False)
    status=models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return self.FIR_No

class Message(models.Model):
    full_name=models.CharField(max_length=120, blank=False, null=False)
    email=models.EmailField()
    rank=models.CharField(max_length=10)
    badge_no=models.CharField(max_length=10)
    message=models.CharField(max_length=320, blank=False, null=False)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    read_status=models.BooleanField(default=False, blank=True)



class CustomUserManager(BaseUserManager):

    def _create_user(self, username, password,
                     is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
       
        user = self.model(username=username, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now,
            date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True,
                                 **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):

    username=models.CharField(_('username'), max_length=32, unique=True)
    email = models.EmailField(_('email address'), max_length=254)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    
    rank=models.CharField(max_length=10)
    badge_no=models.CharField(max_length=10)

    is_staff = models.BooleanField(_('staff status'), default=False)
    
    is_active = models.BooleanField(_('active'), default=True)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


