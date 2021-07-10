from django.db import models
from django.contrib.auth import base_user


class UserModel(base_user.AbstractBaseUser):
    """
    A user of Itzhak. A user can perform CRUD actions around expenses,
    profile, and budgets.
    """

    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    balance = models.FloatField(default=0, blank=True)
