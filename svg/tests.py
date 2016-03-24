import os
from django.conf import settings
from django.template import Context, Template
from django.test.testcases import SimpleTestCase

from svg.exceptions import SVGNotFound


class SVGTemplateTagTest(SimpleTestCase):

    def test_should_render_svg(self):
        svg_file = open(os.path.join(settings.BASE_DIR,
                                     'static',
                                     'svg',
                                     'django.svg')).read()
        template = Template("{% load svg %}{% svg 'django' %}")

        self.assertEqual(svg_file, template.render(Context()))

    def test_when_given_invalid_file_it_should_fail_silently(self):
        template = Template("{% load svg %}{% svg 'thisdoesntexist' %}")

        self.assertEqual('', template.render(Context()))

    def test_when_debug_it_should_raise_an_error(self):
        template = Template("{% load svg %}{% svg 'thisdoesntexist' %}")

        with self.settings(DEBUG=True):
            with self.assertRaises(SVGNotFound):
                template.render(Context())
