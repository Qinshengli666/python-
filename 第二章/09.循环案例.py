

ok_username='123'
ok_password='123'

while True:
    username = input("输入账号：")
    password = input("输入密码：")
    if ok_username == username and ok_password == password :
        print("登入成功")
        break
    else:
        print("重新输入")