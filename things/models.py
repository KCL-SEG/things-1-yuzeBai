from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Thing(BaseUserManager):
    name = models.CharField(
        max_length=30,
        unique=True,
        #blank=False
    )
    description = models.CharField(
        max_length=120,
        blank = True
    )
    quantity = models.IntegerField(
        blank = True,
        default=1,
        validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
        ]
    )
    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'description', 'quantity']

    def create_thing(self, name, description, quantity):
        user = self.model(name=name, description=description, quantity=quantity)
