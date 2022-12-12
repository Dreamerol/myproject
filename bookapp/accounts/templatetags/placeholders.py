from django.template import Library

register = Library()


@register.filter
def placeholder(field, text):
    field.field.widget.attrs['placeholder'] = text
    return field
