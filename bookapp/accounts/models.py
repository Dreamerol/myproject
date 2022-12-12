from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from bookapp.core.utils import validate_only_letters


# class Gender(Enum):
#     male = 'Male'
#     female = 'Female'
#     dontshow = 'Do not show'
#
#     @classmethod
#     def show(cls):
#         return [(x.name, x.value) for x in cls]
# Create your models here.
class AppUser(AbstractUser):
    first_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
                    )
        )

    last_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )
    # gender = models.CharField(
    #     choices=Gender.show()
    # )

