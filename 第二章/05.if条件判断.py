# num = 900
#
# if num > 700:
#     print("欢迎")


# ok_name = '123'
#
# ok_password = '123'
#
# name = input("输入账号")
# password = input("输入密码")
#
# if ok_name == name and ok_password == password:
#
#     print("登入成功")
# else:
#     print("账号或密码错误")


num = int(input("输入一个数"))

if num > 0:
    print(f"{num}是正数")
elif num < 0:
    print(f"{num}是负数")
elif num == 0:
    print(f"{num}是0")

