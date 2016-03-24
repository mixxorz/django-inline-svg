import os
import sys

import django
from django.conf import settings


DIRNAME = os.path.dirname(__file__)
settings.configure(DEBUG=True,
                   DATABASE_ENGINE='sqlite3',
                   DATABASE_NAME=os.path.join(DIRNAME, 'database.db'),
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'svg',))

try:
    # Django <= 1.8
    from django.test.simple import DjangoTestSuiteRunner
    test_runner = DjangoTestSuiteRunner(verbosity=1)
except ImportError:
    # Django >= 1.8
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner(verbosity=1)
    django.setup()

failures = test_runner.run_tests(['svg'], verbosity=1)
if failures:
    sys.exit(failures)
