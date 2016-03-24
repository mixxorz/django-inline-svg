from os import chdir
from os.path import abspath, dirname, join, normpath
from setuptools import find_packages, setup

with open(join(dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


# allow setup.py to be run from any path
chdir(normpath(abspath(dirname(__file__))))

import svg  # noqa

setup(
    name='django-inline-svg',
    version=svg.__version__,
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    license=svg.__license__,
    description=svg.__doc__,
    long_description=README,
    url='https://github.com/mixxorz/django-inline-svg',
    author='Mitchel Cabuloy',
    author_email='mixxorz@gmail.com',
    maintainer='Mitchel Cabuloy',
    maintainer_email='mixxorz@gmail.com',
    install_requires=[
        'Django>=1.8'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='tests',
)
