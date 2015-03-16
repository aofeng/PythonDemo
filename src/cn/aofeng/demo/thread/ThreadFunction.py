#coding:utf8
#多线程最简单的调用方式，使用thread.start_new_thread来调用函数：
# 第一个参数是被调用的函数；
# 第二个参数是传递给被调用函数的参数列表，必须是Tuple数据类型。
import thread
import time

def add(num):
    i = 0
    result = 0;
    while i<=num:
        result  += i
        i += 1
    print "result=",result

thread1ID = thread.start_new_thread( add, (100,) )
thread2ID = thread.start_new_thread( add, (100,) )

time.sleep(3)   # 休眠一会等待前面启动的两个线程执行结束
