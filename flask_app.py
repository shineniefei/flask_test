#!/usr/bin/env python3
# coding:utf-8

import os
import sys
from flask import Flask, jsonify, request, Response
from conf.config import config_dict

# add current_path to os path first
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def create_app(config=None):

    app = Flask(
        __name__,
        instance_relative_config=True,
    )
    # config
    if config is None:
        app.config.from_object(config_dict['dev'])
        # app.config.from_pyfile('dev.py')
        app.logger.info('config is dev')
    else:
        app.config.from_object(config_dict[config])
        # app.config.from_pyfile(config + '.py')

    app.config.from_envvar('APP_CONFIG', silent=True)

    # root route
    @app.route('/', methods=['GET', 'POST'])
    def index():
        back = {}
        if request.method == 'POST':
            if request.content_type == 'application/x-www-form-urlencoded':
                data = request.form
            elif request.content_type == 'application/json':
                data = request.data.decode('utf-8')
            else:
                data = request.values
            app.logger.info(f'index request method: POST, data: {data}')
            back['postmsg'] = data
        else:
            data = request.values
            # data = request.args
            app.logger.info(f'index request method: GET, data: {data}')
            back['getmsg'] = data
        app.logger.info(f'index response data: {back}')
        return jsonify(back)

    # favicon route
    @app.route('/favicon.ico')
    def favicon():
        return Response('/static/img/favicon.ico', mimetype="image/ico")

    return app


# executing code in a module when it is run as a script or with python -m but not when it is imported
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001)
