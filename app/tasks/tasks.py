#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import celery
from celery.utils.log import get_task_logger
import time
logger = get_task_logger(__name__)

# 定时导入
current_time = str(time.strftime('%Y-%m-%d %H:%M:%S'))
@celery.task(name="task1")
def task1():
    print u"定时任务task1：每5秒执行一次" + current_time
    # 记录日志
    logger.info(u"导入成功")


@celery.task(name="task2")
def task2():
    # 记录日志
    print u"定时任务task2：每10秒执行一次" + current_time 
    logger.info(u"echo成功")



