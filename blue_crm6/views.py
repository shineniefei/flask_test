#!/usr/bin/env python3
# coding:utf-8

from flask import Blueprint
from flask import request
from flask import current_app
from flask import jsonify

with current_app.app_context():
    pass

crm6 = Blueprint('crm6', __name__)


@crm6.route('/', methods=['GET', 'POST'])
def home():
    back = {}
    if request.method == 'POST':
        if request.content_type == 'application/x-www-form-urlencoded':
            data = request.form
        elif request.content_type == 'application/json':
            data = request.data.decode('utf-8')
        else:
            data = request.values
        crm6.logger.info(f'index request method: POST, data: {data}')
        back['postmsg'] = data
    else:
        data = request.values
        crm6.logger.info(f'index request method: GET, data: {data}')
        back['getmsg'] = data
    crm6.logger.info(f'index response data: {back}')
    return jsonify(back)