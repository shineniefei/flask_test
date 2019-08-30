#!/usr/bin/env python3
# coding:utf-8

import os
import sys
from flask import Flask, jsonify, request
from flask_spyne import Spyne

# add current_path to path first
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_BLUEPRINTS = (
    ("flask_test.blue.blue_crm6", "crm6", "crm6"),
    ("flask_test.blue.blue_web", "web", "web"),
    ("flask_test.blue.blue_mock", "mock", "mock"),
)


def create_app(config=None):

    app = Flask(
        __name__,
        instance_relative_config=True,
    )

    spyne = Spyne(app)

    from blue_mock.views import mock
    app.register_blueprint(mock, url_prefix='/mock')

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
            app.logger.info(f'index request method: GET, data: {data}')
            back['getmsg'] = data
        app.logger.info(f'index response data: {back}')
        return jsonify(back)

    return app


# When the module is directly run, the under code will be run
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001)
