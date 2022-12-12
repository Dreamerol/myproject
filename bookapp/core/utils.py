from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if ch.is_not_alpha():
            raise ValidationError('Only letters are allowed!')