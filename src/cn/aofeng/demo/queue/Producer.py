#coding:utf8
import threading

class Producer(threading.Thread):
    ''' 简单的生产者：往队列放数据'''
    
    def __init__(self, queue, yieldNum):
        super(Producer, self).__init__()
        self.setName("Producer")
        self.__queue = queue
        self.__yieldNum = yieldNum

    def run(self):
        i = 0
        while i<self.__yieldNum:
            self.__queue.put( "product, num"+str(i) )
            i += 1
        self.__queue.put("exit")   # 退出指令，消费者收到此数据会退出
            