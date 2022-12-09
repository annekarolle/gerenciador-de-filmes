from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)
    is_employee = models.BooleanField(default=False, blank=True)
    is_superuser =  models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f"User - email:{self.email} - id:{self.id}"

