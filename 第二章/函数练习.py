# 函数练习
#
# 需求：实现各种实用函数
# 思路：1) 实现计算函数（加减乘除）2) 实现字符串处理函数 3) 使用lambda简化代码
# 递归练习


def jia (x,y) :
    return x+y
print(jia(2,3))

def jia (x,y) :
    return x-y
print(jia(2,3))

def jia (x,y) :
    return x*y
print(jia(2,3))

def jia (x,y) :
    return x/y
print(jia(2,3))


s = lambda x,y : x+y

print(s(1,2))

print("------------------------------")

def jc (i) :

    if i == 1:
        return 1
    else:

       return   i * jc(i - 1)




print(jc(5))


