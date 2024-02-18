from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self):
        pass

    def create_superuser(self):
        pass


class User(AbstractBaseUser):
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)

    objects = UserManager

    USERNAME_FIELD = email
    REQUIRED_FIELDS = []

    def __str__(self):
        pass

    def is_staff(self):
        pass
