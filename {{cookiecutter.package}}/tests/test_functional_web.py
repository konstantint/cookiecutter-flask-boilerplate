# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: functional web tests

See http://webtest.readthedocs.org/

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""


def test_login(testapp):
    # Not logged in initially
    res = testapp.get("/")
    res.mustcontain("You can try to")

    # Cannot access admin
    res = testapp.get("/admin/")
    assert res.status_code == 302
    res = res.follow()
    res.mustcontain("Please, authenticate")

    # Try logging in with wrong password
    res = testapp.get("/auth/login")
    res.mustcontain("Please, authenticate")
    form = res.forms[0]
    form['login'] = 'admin'
    form['password'] = 'wrong'
    res = form.submit()
    res.mustcontain("Invalid password")

    # Try logging in with correct password
    form = res.forms[0]
    form['login'] = 'admin'
    form['password'] = 'admin'
    res = form.submit().follow()
    res.mustcontain("Hi, admin")

    # Confirm we can access admin
    res = testapp.get("/admin/")
    assert res.status_code == 200
