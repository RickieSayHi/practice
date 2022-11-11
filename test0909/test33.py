"""
创建一个类
"""


# 设计一个类
class Student:
    name: None  # 记录学生姓名
    gener: None  # 记录学生性别
    age: None  # 记录学生年龄
    nationality: None  # 记录学生国籍
    native_place: None  # 记录学生籍贯

    def say_hi(self):
        print(f"嗨，大家好，我是{self.name}")


stu = Student()

stu.name = "张晓军"
stu.gener = "男"
stu.age = 19
stu.nationality = "中国"
stu.native_place = "安徽"

print(f"打印学生信息： {stu} 类型为：{type(stu)}")
print(stu.name)
print(stu.gener)
print(stu.age)
print(stu.nationality)
print(stu.native_place)

stu.say_hi()


class Clock:
    id: None
    price: None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = "034201"
clock1.price = 23.45

clock1.ring()
