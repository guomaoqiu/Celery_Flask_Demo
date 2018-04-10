# -*- coding: utf-8 -*-
from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
import time
from .. import db
logger = get_task_logger(__name__)
from ..models import ApiTest


@periodic_task(run_every=50)
#@periodic_task(run_every=crontab(minute='*', hour='*', day_of_week="*"))

def periodic_task1():
    """
    @summary: 周期性任务执行函数
    """
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    try:
        import requests
        req = requests.get('http://www.baidu.com')
        print req.status_code
        logger.info(u"Celery 周期任务调用成功，当前时间：{}".format(now))
    except Exception:
        logger.error(u"Celery 周期任务调用失败，当前时间：{}".format(now))


@periodic_task(run_every=5)
def apitest():
    """
    @summary: 周期性任务执行函数
    """

    import random
    res= random.randint(0,99)
    #print res


    each_info = ApiTest(name=str(res))
    try:
        db.session.add(each_info)
        db.session.commit()
    except Exception,e:
        db.session.rollback()
        print e
    


    

