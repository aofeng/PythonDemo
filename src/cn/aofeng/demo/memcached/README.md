#预备
* Python 2.7
* Memcached 1.4.x
* python-memcached-1.54

#安装
1、下载源码包。
```bash
wget http://ftp.tummy.com/pub/python-memcached/old-releases/python-memcached-1.54.tar.gz
```

2、解压缩。
```bash
tar -zxvf python-memcached-1.54.tar.gz
```

3、安装。
```bash
python setup.py install
```
注：需要root权限

#编程
```Python
#coding:utf8
import memcache

class MemcachedClient():
    ''' python memcached 客户端操作示例 '''
    
    def __init__(self, hostList):
        self.__mc = memcache.Client(hostList);
    
    def set(self, key, value):
        result = self.__mc.set("name", "NieYong")
        return result
    
    def get(self, key):
        name = self.__mc.get("name")
        return name
    
    def delete(self, key):
        result = self.__mc.delete("name")
        return result

if __name__ == '__main__':
    mc = MemcachedClient(["127.0.0.1:11511", "127.0.0.1:11512"])
    key = "name"
    result = mc.set(key, "NieYong")
    print "set的结果：", result
    name = mc.get(key)
    print "get的结果：", name
    result = mc.delete(key)
    print "delete的结果：", result
```

执行脚本的结果:
```
set的结果： True
get的结果： NieYong
delete的结果： 1
```
