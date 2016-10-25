from __future__ import absolute_import
import logging
import os

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.exceptions import ImproperlyConfigured
from django.utils.safestring import mark_safe

from svg.exceptions import SVGNotFound

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def svg(filename):
    SVG_DIRS = getattr(settings, 'SVG_DIRS', [])

    if type(SVG_DIRS) != list:
        raise ImproperlyConfigured('SVG_DIRS setting must be a list')

    path = None

    if SVG_DIRS:
        for directory in SVG_DIRS:
            svg_path = os.path.join(directory, '%s.svg' % filename)
            if os.path.isfile(svg_path):
                path = svg_path
    else:
        path = finders.find(os.path.join('svg', '%s.svg' % filename), all=True)

    if not path:
        message = "SVG '%s.svg' not found" % filename

        # Raise exception if DEBUG is True, else just log a warning.
        if settings.DEBUG:
            raise SVGNotFound(message)
        else:
            logger.warning(message)
            return ''

    # Sometimes path can be a list/tuple if there's more than one file found
    if isinstance(path, (list, tuple)):
        path = path[0]

    with open(path) as svg_file:
        svg = mark_safe(svg_file.read())

    return svg
