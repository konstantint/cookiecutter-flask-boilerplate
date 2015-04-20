# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: Flask-Assets integration

See: http://flask-assets.readthedocs.org/

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
from flask_assets import Bundle, Environment

# CSS and JS, local to the developed app
css_local = Bundle(
    "css/style.css",
    filters="cssmin",
    output="public/css/local.css"
)

js_local = Bundle(
    "js/plugins.js",
    "js/script.js",
    filters='jsmin',
    output="public/js/local.js"
)

# CSS and JS coming from third-party packages (e.g. Bootstrap / jQuery)
css_thirdparty = Bundle(
    "libs/bootstrap/dist/css/bootstrap.css",
    filters="cssmin",
    output="public/css/thirdparty.css"
)

js_thirdparty = Bundle(
    "libs/jQuery/dist/jquery.js",
    "libs/bootstrap/dist/js/bootstrap.js",
    filters='jsmin',
    output="public/js/thirdparty.js"
)



assets = Environment()
assets.register("js_local", js_local)
assets.register("css_local", css_local)
assets.register("js_thirdparty", js_thirdparty)
assets.register("css_thirdparty", css_thirdparty)

# Although having local copies is great for development,
# It makes sense to serve third party scripts from a common CDN whenever possible.
# The current set up is that the config variable USE_CDN_ASSETS will switch between
# using js_thirdparty / css_thirdparty and js_thirdparty_cdn / css_thirdparty_cdn
# You may want to change this logic to something else. Edit templates/base.html in this case.
js_thirdparty_cdn = ["//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js",
                     "//netdna.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"]
css_thirdparty_cdn = ["//netdna.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"]

def init_app(app):
    assets.init_app(app)

    if app.config['USE_CDN_ASSETS']:
        app.config['js_thirdparty_cdn'] = js_thirdparty_cdn
        app.config['css_thirdparty_cdn'] = css_thirdparty_cdn
