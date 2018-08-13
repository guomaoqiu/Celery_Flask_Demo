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
    MAIL_PASSWORD = '' #os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = u''
    FLASKY_MAIL_SENDER = '2399447849@qq.com'
    FLASKY_ADMIN = '2399447849@qq.com' # os.environ.get('FANXIANG_ADMIN')

    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERYBEAT_SCHEDULE = {
    ＃ 定义任务名称：task1、task2
    ＃ 执行规则：通过timedelta定义
        'task1': {
            'task': 'task1',
            'schedule': timedelta(seconds=5)
         },
        'task2': {
            'task': 'task2',
            'schedule': timedelta(seconds=10)
         }
    }
    

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    '''
    # 创建数据库时需要指定编码为UTF8;
    # CREATE DATABASE `celery` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    # grant all on celery.* to celery@'127.0.0.1' identified by 'celery';
    # flush privileges;
    #
    #python manage.py shell #创建用户角色对应表
    from manager import Role
    Role.insert_roles()
    Role.query.all()
    [<Role u'Moderator'>, <Role u'Administrator'>, <Role u'User'>]
    '''
    DEBUG = True
    db_host = '127.0.0.1'
    db_user = 'celery'
    db_pass = 'celery'
    db_name = 'celery'
    SQLALCHEMY_DATABASE_URI = 'mysql://' + db_user + ':' + db_pass + '@' + db_host + '/' + db_name
    #SQLALCHEMY_ECHO=False #用于显式地禁用或启用查询记录




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
