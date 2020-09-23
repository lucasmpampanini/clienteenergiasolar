from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def format_brl(value):
    value = round(float(value), 2)
    value = "R$%s%s" % (intcomma(int(value)), ("%0.2f" % value)[-3:])
    return ''.join((value[:-3], ",", value[-2:]))