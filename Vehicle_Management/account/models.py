from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_superadmin = models.BooleanField('Is Super Admin',default=False,)
    is_admin = models.BooleanField('Is Admin', default=False,)
    is_user = models.BooleanField('Is User', default=False)
