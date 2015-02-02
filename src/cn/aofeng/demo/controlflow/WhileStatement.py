#coding:utf-8
# 循环控制语句：while

from cn.aofeng.demo import Guess

running = True
while running:
    result = Guess.guess(9)
    if result:
        break

print("Done")
