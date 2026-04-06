from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customers")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
