from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models

from auth_demos.auth_app.managers import AppUsersManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'
    objects = AppUsersManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

