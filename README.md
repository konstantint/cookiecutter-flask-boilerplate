Flask-Boilerplate cookiecutter template
========================================

This is a [CookieCutter](http://pydanny.com/cookie-project-templates-made-easy.html) template for generating a generic Flask project. It provides simple starting points for using some of the popular best-practices:

  * Proper [setuptools](https://pypi.python.org/pypi/setuptools)-compatible package layout.
  * Several of nearly-standard extensions (Flask-SQLAlchemy, Flask-Login, Flask-Admin, Flask-Script)
  * [py.test](http://pytest.org/)-based tests.
  * Usage of the [Travis-CI](https://travis-ci.org/) continuous integration service.

Installation
------------

Before you can use this template you should install ``cookiecutter`` via ``easy_install`` or ``pip``:

    $ pip install cookiecutter

The ``cookiecutter`` executable should appear in your Python's ``bin/`` (in Windows ``Scripts/``) directory. You might need to add that directory to your ``PATH`` to run the executable. You should also have ``git`` installed in your system.

Usage
-----

To initialize a new project, ensure that ``cookiecutter`` is in your path and run:

     $ cookiecutter https://github.com/konstantint/cookiecutter-flask-boilerplate.git

After asking some basic questions, the tool will create the following project layout for you::

    <package_root>/
    |
    +-- .gitignore              # Git configuration
    +-- .travis.yml             # Travis-CI configuration
    +-- .bowerrc                # Bower configuration
    +-- bower.json              # Javascript dependencies (using Bower)
    +-- setup.cfg               # Configuration for py.test and other tools
    +-- setup.py                # Package metadata
    +-- MANIFEST.in             # Files to include in the package
    +-- README.rst              # Package description
    +-- LICENSE.txt             # License text (MIT, replace if not applicable)
    +-- CHANGELOG.txt           # Changelog
    +-- requirements.txt        # List of "last known good" versions of package dependencies
    +-- sample_pasteconfig.ini  # Sample config for Webapp deployment using PasteDeploy
    +-- sample_settings.py      # Sample configuration file
    |
    +-- tests/                  # PyTest-based tests
    |   |
    |   +-- conftest.py         # Global test configuration and fixtures
    |   +-- test_***.py         # Sample tests
    |
    +-- <package>/              # Package code root directory
        |
        +-- static/             # Flask static directory.
        +-- templates/          # Jinja2 templates
        +-- views/              # Views (index, login, admin)
        |
        +-- app.py              # Flask app configuration
        +-- manage.py           # Flask-Script management script
        +-- model.py            # Flask-SQLAlchemy data model
        +-- config.py           # Configuration logic
        +-- i18n.py             # Flask-Babel
        +-- assets.py           # Flask-Assets

Typically you would want to add the newly created project to the version control before doing anything else:

    $ git init
    $ git add .
    $ git commit -m "Initial package structure"

To give a quick test run of the resulting project, proceed as follows:

    $ python setup.py develop
    $ <project>-manage createdb
    $ <project>-manage assets build
    $ <project>-manage runserver


Common development tasks
------------------------

  * **Specifying a local configuration**

        $ cp sample_settings.py settings.py
        ... edit settings.py ...
        $ export CONFIG=/path/to/settings.py  
        ... (can be just "settings.py",
         if you plan to run everything from the same directory) ...

  * **Testing**

        $ py.test
        .. or ..
        $ python setup.py test

  * **Specifying dependencies for your package**  
    Edit the ``install_requires`` line in ``setup.py`` by listing all the dependent packages.

  * **Using the debug shell**
    Run ``<project>-manage shell``. The resulting shell provides variables ``app``, ``model`` and ``db`` for convenience.

  * **Publishing the package on Pypi**

        $ python setup.py register sdist upload

  * **Travis-CI integration**  
    To use the [Travis-CI](https://travis-ci.org/) continuous integration service, follow the instructions at the [Travis-CI website](https://travis-ci.org/) to register an account and connect your Github repository to Travis. The boilerplate code contains a minimal `.travis.yml` configuration file that might help you get started.

See also
--------
  * [CookieCutter-Flask template](https://github.com/sloria/cookiecutter-flask)
  * [Flask-Heroku template](https://github.com/zachwill/flask_heroku)
  * [Python-Boilerplate template](https://github.com/konstantint/cookiecutter-python-boilerplate)


Copyright & License
-------------------

  * Copyright 2015, Konstantin Tretyakov
  * License: MIT
