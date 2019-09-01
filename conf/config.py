#!/usr/bin/env python3
# coding:utf-8

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'formatters': {
        # 啰嗦的日志格式
        'verbose': {
            'format':
            '%(asctime)s [%(levelname)s] [%(threadName)s:%(thread)d] [%(name)s:%(funcName)s:%(lineno)d] - %(message)s'
        },
        # 简单的日志格式
        'simple': {
            'format': '%(asctime)s [%(levelname)s] [%(name)s] - %(message)s'
        },
    },
    'handlers': {
        'default': {
            # 'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 循环日志
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,  # 备份数量
            'filename': BASE_DIR + '/logs/flask_test.log',  # 日志保存文件
            'formatter': 'verbose',  # 日志格式，与上边的设置对应选择
            'encoding': 'utf-8',
        },
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
        'development': {
            'handlers': ['default'],
        },
        'production': {  # 日志记录器
            'handlers': ['error'],
            'level': 'INFO',
        }
    },
}

class Config(object):
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    LOGGING = LOGGING['handlers']['default']


class DevelopConfig(Config):
    CONF = 'DevelopConfig'
    DEBUG = True
    ENV = 'development'
    TESTING = True
    LOGGING = LOGGING['handlers']['default']


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
