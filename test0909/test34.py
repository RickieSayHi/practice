"""
类对象 中的构造方法  __init__
"""
import random


class Student:
    def __init__(self, name, age, tel):
        # 这一步既有赋值功能，也有声明功能
        self.name = name
        self.age = age
        self.tel = tel
        print("初始化类对象")

    def __str__(self):
        return f"Student类对象，name = {self.name}, age = {self.age}, tel = {self.tel}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("林俊杰", 19, "18900004444")
print(stu1.name)
print(stu1.age)
print(stu1.tel)

stu2 = Student("周杰伦", 18, "18700002233")
print(stu2.name)
print(stu2.age)
print(stu2.tel)

stu3 = Student("张学友", 18, "18700002453")
print(stu3.name)
print(stu3.age)
print(stu3.tel)

print(stu1)
print(str(stu1))
print(stu2)
print(str(stu2))
print(stu3)
print(str(stu3))

print(f"大小比较 stu1 < stu2 :  {stu1 < stu2}")
print(f"大小比较 stu1 <= stu2 :  {stu2 <= stu3}")


def func(data: str):
    print(f"打印日志： {data}")


func("djdjjd")


def add(x: int, y: int) -> int:
    sum_io = random.randint(x, y)
    return x + y + sum_io


a = add(3, 6)

print(f"打印 结果 ： {add(2, 10)}")
