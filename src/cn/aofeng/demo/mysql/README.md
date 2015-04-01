#预备
Python 2.7
Connector/Python 2.1.1

#安装
1、下载源码包。
```bash
wget http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.1.tar.gz
```

2、解压缩。
```bash
tar -zxvf mysql-connector-python-2.1.1.tar.gz
```

3、安装。
```bash
python setup.py install
```
注：**需要root权限**

#编程
```Python
#coding:utf8
# 使用 Connector/Python 进行查询操作。
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
```

#问题
##umask导致的问题
我的开发服务器默认的umask设置为0037，结果安装后，在root用户下可以正常地使用mysql.connector模块，但是切换至其他的普通账号时，会报错：
`ImportError: No module named mysql.connector`

**解决方法：**
在执行`python setup.py install`之前，先执行`umask 0022`。

#参考资料
* [Installing Connector/Python from a Source Distribution](http://dev.mysql.com/doc/connector-python/en/connector-python-installation-source.html)
* [Connecting to MySQL Using Connector/Python](http://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
