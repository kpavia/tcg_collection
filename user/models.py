from django.db import models
from django.contrib.auth.models import User


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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
