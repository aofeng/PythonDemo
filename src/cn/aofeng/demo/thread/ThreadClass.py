#coding:utf8
# 继承threading.Thread创建类，由类的start方法调用run方法启动线程。
import threading
import time

class SleepThread(threading.Thread):
    
    def __init__(self):
        super(SleepThread, self).__init__()

    def run(self):
        time.sleep(10)   # 休眠10秒，模拟耗时操作


if __name__ == "__main__":
    thread1 = SleepThread()
    thread2 = SleepThread()
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
