#!/usr/bin/env python3
# coding:utf-8

import os

from flask import Blueprint
from flask import render_template
from flask import send_file
from flask import send_from_directory

# new blueprint object as web
web = Blueprint(
    'web', __name__, static_folder='static', static_url_path='/web/static')


# blueprint root route
@web.route('/', methods=['GET', 'POST'])
def home():
    return web.send_static_file('index.html')  # html在static文件夹下
    # return render_template('index.html')


# send back html
@web.route('/<html>', methods=['GET', 'POST'])
def html(html):
    return web.send_static_file(html + '.html')


# send back template
@web.route('/<temp>', methods=['GET', 'POST'])
def temp(temp):
    return render_template(html + '.html')


# send back file with name
@web.route('/static/<staticfile>', methods=['GET', 'POST'])
def staticfile(staticfile):
    return send_file(staticfile)


# send back js file
@web.route('/static/js/<jsfile>', methods=['GET', 'POST'])
def js(jsfile):
    return web.send_static_file('js/' + jsfile)


# current file path
file_path = os.path.dirname(os.path.abspath(__file__))


# send back img file
@web.route('/static/img/<imgfile>', methods=['GET', 'POST'])
def img(imgfile):
    return send_from_directory(file_path, 'static/img/' + imgfile)
