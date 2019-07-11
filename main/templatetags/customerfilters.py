from django import template

register = template.Library()

@register.filter
def to_percent(my_float):
    return "{:.5%}".format(my_float)
