#coding:utf8
# 使用Python标准库操作JSON
import json

# ========== encode ==========
# 将Dictionary转换成json字符串
peoples = {
    "张三":{"name":"张三", "sex":"男", "age":20},
    "如花":{"name":"如花", "sex":"女", "age":30}
}
print json.dumps(peoples)

# 将List转换json字符串
fruits = ["Apple", "Orange", "Watermelon"]
print json.dumps(fruits)

# ========== decode ==========
# 将JSON字符串转换成对象
fo = open("JsonSample.txt", "rb")
jsonStr = fo.read()
fo.close()

obj = json.loads(jsonStr)
print obj.get("game").get("apkChannelId")
print obj.get("game")
print obj.get("id")
print obj
