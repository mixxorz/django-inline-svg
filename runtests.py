import os
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner


DIRNAME = os.path.dirname(__file__)
BASE_DIR = os.path.abspath(DIRNAME)
settings.configure(
    BASE_DIR=BASE_DIR,
    DEBUG=True,
    DATABASE_ENGINE='sqlite3',
    DATABASE_NAME=os.path.join(DIRNAME, 'database.db'),
    INSTALLED_APPS=('django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.staticfiles',
                    'django.contrib.admin',
                    'svg',),
    STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')],
    STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles'),
    STATIC_URL='/static/',
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.i18n',
                    'wagtail.contrib.settings.context_processors.settings',
                    'apps.shop.context_processors.collections',
                ],
            },
        },
    ]
)
django.setup()

test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['svg'], verbosity=1)
if failures:
    sys.exit(failures)
