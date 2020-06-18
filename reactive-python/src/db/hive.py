#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hive util with hive server2
import datetime

from pyhive import hive

conn = hive.Connection(host='192.168.**.**', port=10000, database='tmp')
# host主机ip,port：端口号，username:用户名，database:使用的数据库名称
cursor = conn.cursor()
sql = 'select * from tablename limit 10'
start_time = datetime.datetime.now()
cursor.execute(sql)  # 执行查询
for result in cursor.fetchall():
    print(result)  # 将查询结果打印出来
end_time = datetime.datetime.now()
print("查询时间：" + str((end_time - start_time).total_seconds()) + "s", end='  ')
