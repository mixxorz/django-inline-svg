import logging
import os

from django import template
from django.contrib.staticfiles import finders
from django.utils.safestring import mark_safe

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def svg(filename):
    path = finders.find(os.path.join('svg', '%s.svg' % filename), all=True)

    if isinstance(path, (list, tuple)):
        path = path[0]

    if not path:
        logger.warning('SVG %s not found' % filename)
        return ''

    with open(path) as svg_file:
        svg = mark_safe(svg_file.read())

    return svg
