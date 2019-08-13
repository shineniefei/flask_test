#!/usr/bin/env python3
# coding:utf-8

import os
from instance import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # 啰嗦的日志格式
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] - %(message)s'
        },
        # 简单的日志格式
        'simple': {
            'format': '%(asctime)s [%(levelname)s] [%(name)s] - %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()':
            'django.utils.log.RequireDebugTrue',  # 过滤器，只有当setting的DEBUG = True时生效
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False,
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'default': {  # 重点配置部分
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 循环日志
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,  # 备份数量
            'filename': BASE_DIR + '/logs/flask_test.log',  # 日志保存文件
            'formatter': 'verbose',  # 日志格式，与上边的设置对应选择
            'encoding': 'utf-8',
        },
        # 专门用来记错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',  # 默认一直追加
            'filename': os.path.join(BASE_DIR, 'logs/error.log'),  # 日志文件
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'console'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        'production':
        {  # 日志记录器
            'handlers': ['error', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        }
    },
}


class Config(object):
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    LOGGER_NAME = LOGGING


class DevelopConfig(Config):
    CONF = 'DevelopConfig'
    DEBUG = True
    ENV = 'development'
    TESTING = True
    LOGGER_NAME = LOGGING


class TestConfig(Config):
    CONF = 'TestConfig'
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    CONF = 'ProductionConfig'
    DEBUG = False
    TESTING = False


config_dict = {
    'dev': DevelopConfig,
    'test': TestConfig,
    'prod': ProductionConfig
}
