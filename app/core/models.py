"""
    DataBase Models.
"""

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """ Base User Model Manager """
    def create_user(self, email, password=None, **extra_fields):
        """ Create, save and retrun a new user"""
        if not email:
            raise ValueError("You must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return Super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ User Model """
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    name = models.CharField(_("Name"), max_length=100)
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
