from django.conf import settings
from django_pint.settings import DJANGO_PINT_UNIT_REGISTER

UNITS = {
    "tsp": DJANGO_PINT_UNIT_REGISTER.tsp,
    "tbsp": DJANGO_PINT_UNIT_REGISTER.tbsp,
    "cup": DJANGO_PINT_UNIT_REGISTER.cup,
    "ounce": DJANGO_PINT_UNIT_REGISTER.oz,
    "fluid ounce": DJANGO_PINT_UNIT_REGISTER.floz,
    "liter": DJANGO_PINT_UNIT_REGISTER.liter
}