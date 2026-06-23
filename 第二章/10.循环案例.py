import random

random_num =random.randint(1,100)

while True:
    num=int(input("猜数字："))
    if num>random_num:
        print("大了")
    elif num<random_num:
        print("小了")
    else:
        print("对了")
        break
print(random_num)