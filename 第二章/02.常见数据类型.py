# print("hello python")
# print(type("hello python")) #str
#
# print(type(111)) #int
# print(type(12.1)) #float
# print(type(True)) #bool
# print(type(False)) #bool
# print(type(None))  #NoneType
#
# #isinstance 判断是否是指定类型
# num ="111"
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,bool))
# print(isinstance(num,str))
#
# #字符串
# s1 = "hello python" #双引号
# s2 = 'python' #单引号
# s3 = """
# hello python
#
# hello world
#
# 1111
#
#
# """
# print(s1)
# print(s2)
# print(s3)
#
#
# #转义字符 \' \" \n 换行 \t 缩进
# print("hello\npython\t111")
#
#
# #字符串的拼接  str(int)将int类型数据转为字符串  +只能拼接str类型
#
# name = "张三"
#
# age = 18
#
# pro = "计算机"
#
# hobby = "python , java"
# print("------------------------")
#
# print("大家好 ，我是" + name + "今年" + str(age) + "岁了" + "专业是" + pro + "爱好" + hobby)
#
# #占位符 %s
#
# print("大家好 ，我是 %s , 今年 %s , 岁了专业是 %s , 爱好 %s" % (name , age ,pro , hobby))
#
# #占位符 f
#
# print(f"大家好 ，我是{name},今年{age}岁了,专业是{pro}，爱好{hobby}")
#

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
