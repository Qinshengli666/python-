#
#
#
# 需求：实现完整的教务系统
# 思路：1) 设计学生类 2) 实现添加、删除、修改、查询功能 3) 添加异常处理
from symtable import Class
from unittest import case


class Student :
    def __init__(self,name,age,score) :
        self.name=name
        self.age=age
        self.score=score

class Jwxt :

    def __init__(self) :

        self.st_list=[]


    def tj(self) :

        name = input("输入name")
        age = input("输入age")
        score = int (input("输入score"))

        self.st_list.append(Student(name,age,score))

    def cx(self) :

        for i in self.st_list :
            print(i.name,i.age,i.score)

    def sc(self) :

        self.cx()

        sc_name = input("输入删除的名字：")

        for i in self.st_list :
            if sc_name == i.name :
                self.st_list.remove(i)








xt =Jwxt()
while True :
   print("1.添加学生")

   print("2.删除学生")

   print("3.修改学生")

   print("4.查询学生")

   print("5.退出")

   num = int(input("输入："))

   match num:
       case 1 :
           xt.tj()
       case 2 :
           xt.sc()
       case 3 :
           pass
       case 4 :
           xt.cx()
       case 5:
           break



























