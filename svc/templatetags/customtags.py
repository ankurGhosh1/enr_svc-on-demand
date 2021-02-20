from django import template


register = template.Library()

@register.filter
def userdetails():
    pass