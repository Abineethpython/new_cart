from django import template

register = template.Library()

@register.simple_tag(name='getstatus')
def getstatus(cart):
    status = getattr(cart, 'status', None)
    if status is None or status < 0:
        return "unknown"
    status_array=['confirmed','processed','delivered','rejected']
    return status_array[status]