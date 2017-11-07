from django.core.exceptions import ValidationError
from .login_tests import is_artist_manager
from datetime import date


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


def validate_artist_manager(value, is_artist_manager):
    if not is_artist_manager:
        raise ValidationError(
            '%(value)s is not an artist manager',
            params={'value': value},
        )


def validate_future(value):
    if value < date.today():
        raise ValidationError(
            '%(value)s is in the past',
            params={'value': value},
        )
