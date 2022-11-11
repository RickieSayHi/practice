"""
学生信息录入
开学了有一批学生信息需要录入系统，请设计一个类，记录学生的：
姓名、年龄、地址，这3类信息，
请实现：
1、通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
2、输入完成后，使用print语句，完成信息的输出

当前录入第1位学生信息，总共需录入10位学生信息
请输入学生姓名： 周杰伦
请输入学生年龄： 31
请输入学生地址： 北京
学生1信息录入完成，信息为： 【学生姓名：周杰伦，年龄：31，地址：北京】
当前录入第2为学生信息，总共需录入10位学生信息
请输入学生姓名：
"""


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"姓名为： {self.name}， 年龄为： {self.age}， 地址为： {self.address}"


my_list = []
count = 1
for x in [1, 2, 3]:
    print(x)
    print(f"当前录入第 {count} 位学生信息，总共需录入 {len(my_list)} 位学生信息")
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    address = input("请输入学生地址：")
    stu = Student(name, age, address)
    my_list.append(stu)
    print(f"学生{count}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address} 】")
    count += 1

print(f"一共录入了 {len(my_list)} 位学生信息，信息如下：")
for stu in my_list:
    print(f"{stu}")
