#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2012 Luiz Fernando da Silva <folksilva@gmail.com>

# Importações padrões do python
import os
# Must set this env var *before* importing any part of Django.
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Make sure we can import Django.  We may end up needing to do this
# little dance, courtesy of Google third-party versioning hacks.  Note
# that this patches up sys.modules, so all other code can just use
# "from django import forms" etc.
from google.appengine.dist import use_library
use_library('django','1.2')

import sys
import logging
import __builtin__
import datetime
import time

# Importações do Google App Engine
from google.appengine.ext.webapp import util


import pickle
sys.modules['cPickle'] = pickle

# Enable info logging by the app (this is separate from appserver's
# logging).
logging.getLogger().setLevel(logging.INFO)

# Force sys.path to have our own directory first, so we can import from it.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import the part of Django that we use here.
import django.core.handlers.wsgi

def main():
    # Create a Django application for WSGI.
    application = django.core.handlers.wsgi.WSGIHandler()
    
    # Run the WSGI CGI handler with that application.
    util.run_wsgi_app(application)
    
    #logging.info(datetime.datetime.now())

if __name__ == '__main__':
    main()
