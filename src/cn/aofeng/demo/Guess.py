#coding:utf-8

def guess(num):
    result = False
    enter = int(raw_input("enter a number:"))
    if num == enter:
        print("You are right!")
        result = True
    elif num > enter:
        print("It's lower than that.")
    else:
        print("It's higher than that.")
        
    return result
