#!/usr/bin/env python3
# coding:utf-8

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import current_app
from flask_restful import Api
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from spyne import (Application, Array, ComplexModel, Integer, Iterable,
                   ServiceBase, Unicode, rpc)
from spyne.auxproc.thread import ThreadAuxProc

mock = Blueprint('mock', __name__)
api = Api(mock)


@mock.route('/', methods=['GET', 'POST'])
def home():
    back = {}
    if request.method == 'POST':
        if request.content_type == 'application/x-www-form-urlencoded':
            data = request.form
        elif request.content_type == 'application/json':
            data = request.data.decode('utf-8')
        else:
            data = request.values
        mock.logger.info(f'index request method: POST, data: {data}')
        back['postmsg'] = data
    else:
        data = request.values
        mock.logger.info(f'index request method: GET, data: {data}')
        back['getmsg'] = data
    mock.logger.info(f'index response data: {back}')
    return jsonify(back)

    # 注册路由
    # api.add_resource(TodoList, '/v1/todos', endpoint='todos')
    # api.add_resource(Todo, '/v1/todos/<todo_id>')

    # api.add_resource(TaskListAPI, '/v1/tasks', endpoint='tasks')
    # api.add_resource(TaskAPI, '/v1/tasks/<int:id>', endpoint='task')


class Person(ComplexModel):
    name = Unicode
    age = Integer


class SomeSoapService(spyne.Service):
    __service_url_path__ = '/soap/someservice'
    __in_protocol__ = Soap11()
    __out_protocol__ = Soap11()
    __tns__ = 'http://127.0.0.1/'

    @spyne.srpc(
        Array(Person),  # 请求类型
        _returns=Iterable(Unicode),  # 返回类型
        _in_variable_names={'data': 'param'},  # 请求节点名，默认为函数定义，修改为param
        _out_variable_name='return')  # 返回节点名
    def person(self, data):
        if not data:
            yield 'None'
        for person in data:
            yield 'name is : %s, age is %s.' % (person.name, person.age)

    @spyne.srpc(Integer, _returns=Integer, _out_variable_name='return')
    def block(ctx, seconds):
        print(1)
        return '1'

    __aux__ = ThreadAuxProc(pool_size=1)

    @spyne.srpc(Integer)
    def block(ctx, seconds):
        print(2)