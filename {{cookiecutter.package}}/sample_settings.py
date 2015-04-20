# -*- coding: utf-8 -*-
import os

# Development settings
DEBUG = True
SQLALCHEMY_ECHO = True

# App settings
SECRET_KEY = '<secret value here>'
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db.sqlite')

# Deployment option
DEBUG_SERVER_HOST = '0.0.0.0'
DEBUG_SERVER_PORT = 33300
