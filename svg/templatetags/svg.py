import logging
import os

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.utils.safestring import mark_safe

from svg.exceptions import SVGNotFound

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def svg(filename):
    path = finders.find(os.path.join('svg', '%s.svg' % filename), all=True)

    if not path:
        message = "SVG 'svg/%s.svg' not found" % filename

        if settings.DEBUG:
            raise SVGNotFound(message)
        else:
            logger.warning(message)
            return ''

    if isinstance(path, (list, tuple)):
        path = path[0]

    with open(path) as svg_file:
        svg = mark_safe(svg_file.read())

    return svg
