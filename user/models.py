from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=32, unique=True)
#     first_name = models.CharField(max_length=32)
#     last_name = models.CharField(max_length=32)

#     def create_user(self)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields = ['email', 'username'],
#                 name = 'User model'
#             )
#         ]
