import unittest

from django.template import Context, Template


class SVGTemplateTagTest(unittest.TestCase):

    def test_pass(self):
        template = Template('Hello')

        self.assertEqual('Hello', template.render(Context()))
