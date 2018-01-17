#### Celery + Flask
1. 普通后台任务执行
2. 周期性任务执行

主要是将celery任务执行独立出来；更好的解耦开发

#### 运行:
```
celery worker -l debug -c 100 -A manager.celery -B
-c 执行线程数
-l 输出日志级别
-B 周期性任务参数
```

