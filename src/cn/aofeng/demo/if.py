# 条件控制语句：if elif else
num = 9
enter = int(raw_input("enter a number:"))
if num == enter:
    print("You are right!")
elif num > enter:
    print("It's lower than that.");
else:
    print("It's higher than that.")
print("Done!")
