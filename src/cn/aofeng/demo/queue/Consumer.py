#coding:utf8
import threading
import time

class Consumer(threading.Thread):
    ''' 简单的消费者：从队列中获取数据将显示 '''
    
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.setName("consumer")
        self.__queue = queue

    def run(self):
        while True:
            data = self.__queue.get()
            if "exit" == data:
                print "receive exit command"
                break
            print "receive data:",data
            time.sleep(0.1)
        print "Bye, Bye!"
