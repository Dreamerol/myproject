from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    image_url = models.URLField()


class Book(models.Model):
    title = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(
        max_length=30,
    )



