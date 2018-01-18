#-*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # send mail
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '2399447849@qq.com' #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'Guomaoqiu.310963' #os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = u''
    FLASKY_MAIL_SENDER = '2399447849@qq.com'
    FLASKY_ADMIN = '2399447849@qq.com' # os.environ.get('FANXIANG_ADMIN')

    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    # CELERYBEAT_SCHEDULE = {
    #     #＃ 定义任务名称：task1、task2
    #     #＃ 执行规则：通过timedelta定义
    #     'task1': {
    #         'task': 'task1',
    #         'schedule': timedelta(seconds=5)
    #     },
    #     'task2': {
    #         'task': 'task2',
    #         'schedule': timedelta(seconds=10)
    #     },
    # }


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
 
class ProductionConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
