#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
{{cookiecutter.project}}: setup script

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
import sys
import {{cookiecutter.package}}
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


setup(
    name='{{cookiecutter.package}}',
    version={{cookiecutter.package}}.__version__,
    description="{{cookiecutter.description}}",
    long_description=open("README.rst").read(),
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    url="{{cookiecutter.url}}",
    license='{{cookiecutter.license}}',
    classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Programming Language :: Python'
    ],
    zip_safe=False,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=[
      "Flask", "Flask-SQLAlchemy", "Flask-Login", "Flask-WTF", "Flask-Babel", "Flask-Admin",
      "Flask-Script", "Flask-Assets", "jsmin", "cssmin"
    ],
    tests_require=["pytest", "webtest"],
    cmdclass={'test': PyTest},
    entry_points={
        "console_scripts": ["{{cookiecutter.package}}-manage = {{cookiecutter.package}}.manage:main"],
        "paste.app_factory": ["main = {{cookiecutter.package}}.app:app_factory"]
    },
)
