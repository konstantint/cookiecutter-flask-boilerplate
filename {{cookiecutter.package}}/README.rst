==================================================================
{{cookiecutter.project}}: {{cookiecutter.description}}
==================================================================

This is a "long description" file for the app that you are creating.
If you submit your package to PyPi, this text will be presented on the public page of your package.
Edit it to fit your needs.

Note: This README has to be written using `reStructured Text <http://docutils.sourceforge.net/rst.html>`_, otherwise PyPi won't format it properly.

Installation
------------

The package can be installed by running::

    $ python setup.py install

For development purposes it is often more convenient to use::

    $ python setup.py develop

or, sometimes even::

    $ python setup.py develop --user

If have just created this package from the template or checked it out from version control (rather than used a
pre-built source distribution), you *might* also need to update the Javascript dependencies using `Bower <http://bower.io/>`_::

    $ bower install

In addition, you might need to create the Javascript/CSS asset bundle by running::

    $ {{cookiecutter.package}}-manage assets build

The package can be published on PyPI::

    $ python setup.py sdist register upload

After that, the package will be installable via ``easy_install`` or ``pip``::

    $ easy_install {{cookiecutter.package}}

Usage
-----

The package contains a `Flask <http://flask.pocoo.org/>`_-based web application. Before you can use it, you will need to
perform some preparatory steps.

    1. Copy ``sample_settings.py`` to ``settings.py`` and edit appropriately. Pay attention to debug options and database connection.
    2. Set the environment variable ``CONFIG`` to point to this file::

       $ export CONFIG=/path/to/settings.py

    3. Create the initial database::

       $ {{cookiecutter.package}}-manage createdb

    4. Decide how you would like to run the application. There are multiple options. One is to use the built-in debug server::

       $ {{cookiecutter.package}}-manage runserver

       Another is to serve it using a WSGI container, such as Paste or Gunicorn. We suggest using ``PasteDeploy`` for that::

       $ paste serve sample_pasteconfig.ini

    See ``sample_pasteconfig.init`` for more details.


Development
-----------

In order to understand the package organization it probably makes most sense to start by examining the ``{{cookiecutter.package}}.app`` module.
All other extension modules and blueprints are enabled in the ``create_app`` function there.

The tests should be written in ``tests/``. Those can be run using ``py.test``.

The Javascript and CSS scripts are bundled using Flask-Assets. Each time you change javascript or CSS, you have to rebuild those bundles using::

    $ {{cookiecutter.package}}-manage assets build

Alternatively, you can run a background process that will rebuild everything automatically::

    $ {{cookiecutter.package}}-manage assets watch
