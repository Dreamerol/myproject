# Generated by Django 4.1.4 on 2022-12-11 09:21

import bookapp.core.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), bookapp.core.utils.validate_only_letters]),
        ),
    ]
