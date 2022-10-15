from django.db import models
from user.models import User


class PokemonCard(models.Model):
    name = models.CharField(max_length=64)
    set = models.CharField(max_length=64)
    is_foil = models.BooleanField(null=True)
    value = models.DecimalField(null=True, max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
