from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    gender = models.CharField(max_length=225, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ])
    profilePic = models.ImageField(upload_to="profilePics")

    class Meta:
        db_table = "auth_user"
