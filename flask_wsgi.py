#!/usr/bin/env python3
# coding:utf-8

# from flask_app import app as application

import os
import sys

try:
    from flask_app import create_app
except Exception:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from flask_app import create_app

if len(sys.argv) > 1:
    config = sys.argv[1]
else:
    config = None

# initialize WSGI app object
application = create_app(config)

# uwsgi --http 0.0.0.0:5000 --wsgi-file flask_uwsgi.py --daemonize ./uwsgi.log
# uwsgi --socket 0.0.0.0:5001 --wsgi-file flask_uwsgi.py --daemonize ./uwsgi.log
