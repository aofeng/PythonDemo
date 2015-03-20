#coding:utf8
# 使用Connector/Python进行查询操作

import mysql.connector

# 创建连接
config = {
          'user':'uzone', 
          'password':'uzone', 
          'host':'127.0.0.1', 
          'port':19816,  
          'database':'ucgc_sdk'}
conn = mysql.connector.connect(**config)

# 创建游标
cur = conn.cursor()

# 执行查询SQL
sql = "SELECT notice_id,notice_name,creator,ctime,modifier,mtime FROM notice"
cur.execute(sql)

# 获取查询结果
result_set = cur.fetchall()
if result_set:
    for row in result_set:
        print "%d, %s, %s, %d, %s, %s" % (row[0],row[1],row[2],row[3],row[4],row[5])

# 关闭游标和连接        
cur.close()
conn.close()
