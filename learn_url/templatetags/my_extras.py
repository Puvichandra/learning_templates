from django import template

register = template.library()

@register.filter(name='cut')

def cut(val, arg):
    """
    cuts the word
    """
    return val.replace(arg, '')
