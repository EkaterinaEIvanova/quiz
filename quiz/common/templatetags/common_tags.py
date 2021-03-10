from django import template

register = template.Library()


@register.simple_tag()
def get_name_or_email(user):
    name = user.name if user.name else user.email
    return name
