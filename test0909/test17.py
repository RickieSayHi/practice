"""
练习函数 返回多个返回值
"""


def test_multi_return():
    return 1, "haode", ['2', 3, '4']


x, y, z = test_multi_return()

print(f"函数返回多个返回值： x = {x} , y = {y} , z = {z}")


def user_info(name, age=20, gender='男'):
    print(f"我的名字是 {name}, 年龄是 {age}, 性别是 {gender}")


user_info(name='baibai')
user_info("xixi", 21, '女')
user_info(name='haha', gender='未知')


# 匿名函数， 函数作为参数传入函数中

def test_func(compute):
    result = compute(1, 2)
    print(f"获取到的结果是 : {result}")
    print(f"参数 compute 的类型是 ： {type(compute)}")


def compute(x, y):
    return x + y


test_func(compute)
