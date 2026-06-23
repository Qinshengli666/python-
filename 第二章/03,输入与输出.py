#input 键盘输入
# name = input('请输入name：')
#
# age = input('请输入age：')
#
# print(f'名字 {name} , 年龄 {age}')


#案例  input输入的都是str类型，int()转为int类型

total=1000

password = input("输入密码：")
print(f"密码是：{password}")

num = input("取钱金额：")

print(f"取款{num}剩余{total-int(num)}")
