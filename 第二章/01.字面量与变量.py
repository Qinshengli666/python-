print(100) #整数 int
print(3.13) #浮点 小数 float
print(True) #布尔 bool
print(False) #布尔 bool
print("hello python") #字符串 str
print("------------------")#字符串 str
print(None) #空值 Mone Type

#布尔本质是整数 true=1 flase=0

print(True+1)
print(False-1)


#变量-- python 是动态语言模型. 一个变量可以存储不同数据类型
num = 123.1
print(num)
print(type(num))

print(num+1)

num = "hello python"
print(num)
print(type(num))

num = True
print(num)
print(type(num))


#案例
base = 20.3 #基础播放量

incr = 27 #每一个月的新增播放量

print("未来一个月的总播放量：" , base + incr)
print("未来二个月的总播放量：" , base + incr + incr)
print("未来三个月的总播放量：" , base + incr + incr + incr)


#案例 -- 定义多个变量
base , incr = 20.3 , 27

print("未来一个月的总播放量：" , base + incr)
print("未来二个月的总播放量：" , base + incr + incr)
print("未来三个月的总播放量：" , base + incr + incr + incr)


# 变量赋值
a = 10
b = 20
a , b = b , a
print(a ,b)

#a=100 b=200 c=300  将abc赋值给cab

a = 100
b = 200
c = 300
a ,b ,c =c , b ,a
print("a b c" , a ,b ,c)

