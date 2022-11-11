"""
列表的常用操作（方法）
"""
# List常见的操作

# 通过元素，查找元素的下标
my_list = ["itcast", "itheima", "python"]
index = my_list.index("itheima")
print(f"获取到 itheima 元素的下标为： {index}")

# 通过元素下标，修改元素值
my_list[0] = "传值教育"
print(f"修改后的数组为： {my_list}")

# 插入元素
my_list.insert(1, "best")
print(f"插入元素后的数组为： {my_list}")

# 追加元素
my_list.append("黑马程序员")
print(f"追加元素后的列表为： {my_list}")

# 追加一组元素
my_list2 = ["1", "2", "3"]
my_list.extend(my_list2)
print(f"追加一组元素后的列表为： {my_list}")

# 删除元素：方法一
my_list.pop(1)
print(f"删除元素有的数组为： {my_list}")

# 删除元素：方法二
del my_list[1]
print(f"通过 del 删除 元素后的列表为： {my_list}")

# remove 删除指定元素
my_list = ["itcast", "itheima", "python", "itcast", "itheima", "python"]
my_list.remove("itheima")
print(f"使用 remove 删除指定元素的结果是： {my_list}")

# 清除列表中所有的内容
my_list = ["itcast", "itheima", "python", "itcast", "itheima", "python"]
my_list.clear()
print(f"清空列表后的结果是： {my_list}")

# 统计 元素的 个数
my_list = ["itcast", "itheima", "python", "itcast", "itheima", "python"]
count = my_list.count("itheima")
print(f"统计的元素个数为： {count}")


one_list = [21, 25, 21, 23, 22, 20]
# 1、定义这个列表，并用变量接收它
print(f"定义好的列表为： {one_list}")
# 2、追加一个数字31，到列表的尾部
one_list.append(31)
print(f"追加一个元素后的列表为： {one_list}")
# 3、追加一个新列表[29,33,30]，到列表的尾部
two_list = [29, 33, 30]
one_list.extend(two_list)
print(f"追加一个新列表后的结果为： {one_list}")
# 4、取出第一个元素
first = one_list[0]
print(f"取出第一个元素： {first} 后的列表为： {one_list}")
# 5、取出最后一个元素
last = one_list[-1]
print(f"取出最后一个元素： {last} 后的列表为： {one_list}")
# 6、查找元素31，在列表中的下标位置
index = one_list.index(31)
print(f"元素 31 的下标为： {index}")


three_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp_list = []
temp_for_list = []
print(f"定义列表： {three_list}")
index = 0
while index < len(three_list):
    if three_list[index] % 2 == 0:
        temp_list.append(three_list[index])
    index += 1

print(f"while 循环遍历后， 从 {three_list} 列表中取出偶数， 组成新的列表为： {temp_list}")

for element in three_list:
    if element % 2 == 0:
        temp_for_list.append(element)

print(f"for 循环后，从 {three_list} 列表中取出偶数，组成新列表： {temp_for_list}")
