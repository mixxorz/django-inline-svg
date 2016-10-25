import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
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

    def test_should_load_svg_from_custom_directory(self):
        with self.settings(SVG_DIRS=[os.path.join(settings.BASE_DIR,
                                                  'static', 'custom-dir')]):
            svg_file = open(os.path.join(settings.BASE_DIR,
                                         'static',
                                         'custom-dir',
                                         'other.svg')).read()
            template = Template("{% load svg %}{% svg 'other' %}")

            self.assertEqual(svg_file, template.render(Context()))

    def test_when_given_invalid_file_and_using_custom_directory_it_should_fail(self):  # noqa
        with self.settings(SVG_DIRS=[os.path.join(settings.BASE_DIR,
                                                  'static', 'custom-dir')]):
            template = Template("{% load svg %}{% svg 'nonexistent' %}")

            self.assertEqual('', template.render(Context()))

    def test_when_SVG_DIRS_isnt_a_list_it_should_raise_an_error(self):
        with self.settings(SVG_DIRS=os.path.join(settings.BASE_DIR,
                                                 'static', 'custom-dir')):
            template = Template("{% load svg %}{% svg 'other' %}")

            with self.assertRaises(ImproperlyConfigured):
                template.render(Context())
