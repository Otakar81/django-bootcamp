from django import template

register = template.Library()

def cut(value, arg):
    """
    Elimina la stringa "arg" da value
    """
    return value.replace(arg, '')

# Registro il mio custom tag nella libreria dei template in modo da poterla richiamare
register.filter('cut', cut)