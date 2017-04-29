from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter('parasplit')
@stringfilter
def parasplit_filter(value, autoescape=True):
    return value.rsplit('\n\n')

@register.filter('wordslice')
@stringfilter
def wordslice_(value, arg):
    value = value.split(' ')
    try:
        bits = []
        for x in arg.split(u':'):
            if len(x) == 0:
                bits.append(None)
            else:
                bits.append(int(x))
        return ' '.join(value[slice(*bits)])

    except (ValueError, TypeError):
        return ' '.joint(value)
wordslice_.is_safe = True
