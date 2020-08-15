from django import template
import re
from .. import models

register = template.Library()


@register.filter
def category(format_string):
    categories = models.Category.objects.all()
    return categories