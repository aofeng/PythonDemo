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
