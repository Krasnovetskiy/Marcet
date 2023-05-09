from django.db.models import IntegerChoices


class DiscoundType(IntegerChoices):
    VALUE = 0, 'Value'
    PERCENT = 1, 'Percent'
