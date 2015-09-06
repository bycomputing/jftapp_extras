from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter("parasplit")
@stringfilter
def parasplit_filter(value, autoescape=True):
    paragraph_lines = []
    for line in value.rsplit('\r\n\r\n'):
        if line != '':
            paragraph_lines.append(line)
    return paragraph_lines

@register.filter("wordslice")
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
