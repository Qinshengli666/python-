#
#
# s = 'hello world'
#
# print(s[1])
# print(s[-1])
#
# for i in s:
#     print(i)
#

#
#     样例
#     s.find('Python')在字符串中查找子串，返回第一次出现的索引位置不到返回 - 1
#     s.count('H')统计子串在字符串中出现的次数
#     s.upper()将字符串中的所有字母转换为大写
#     s.lower()将字符串中的所有字母转换为小写
#     s.split(' ') 将字符串按指定分隔符分割成列表
#     s.strip() / s.strip('*') 去除字符串两端的空白字符或指定字符
#     s.replace('H', 'C') 将字符串中的指定子串替换为新的子串
#     s.startwith('P') 检查字符串是否以指定子串开头，返回布尔值
#


#判断是否是回文

s = input("请输入一个字符串：")

if s == s[::-1]:
    print("是回文字符串")
else:
    print("不是回文字符串")

print(s[::-1])


lst = []

for i in range(10):
    s = input(f"请输入第{i+1}个字符串：")
    s = s[::-1].upper()  # 反转并转换为大写
    lst.append(s)

print("处理后的列表内容：")

for item in lst:
    print(item)