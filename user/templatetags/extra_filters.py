from django.template.defaultfilters import register
from datetime import datetime


@register.filter(is_safe=True)
def birth(value):
    year = int(str(value).split("-")[0])
    now = datetime.now().year
    return now - year
