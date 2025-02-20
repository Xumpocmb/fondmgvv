from django import template

register = template.Library()

@register.filter(name='last_segment')
def split(value, arg):
    return value.split(arg)
