import os
import unittest

from django.conf import settings
from django.template import Context, Template


class SVGTemplateTagTest(unittest.TestCase):

    def test_should_render_svg(self):
        svg_file = open(os.path.join(settings.BASE_DIR,
                                     'static',
                                     'svg',
                                     'django.svg')).read()
        template = Template("{% load svg %}{% svg 'django' %}")

        self.assertEqual(svg_file, template.render(Context()))
