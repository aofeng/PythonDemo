#coding:utf8
from cn.aofeng.demo.queue.Consumer import Consumer
import Queue
from cn.aofeng.demo.queue.Producer import Producer

queue = Queue.Queue(1000)
consumer = Consumer(queue)
producer = Producer(queue, 999)

producer.start()
consumer.start()
