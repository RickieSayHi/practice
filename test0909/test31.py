"""
扩展： 列表的sort方法
"""

my_list = [["b", 33], ["c", 22], ["e", 66], ["d", 44], ["a", 55]]


# 定义排序方法
def choose_sort_key(element):
    return element[1]


# 使用带名的函数，定义了函数名的方式
my_list.sort(key=choose_sort_key, reverse=True)

# 使用 lambda 方式
# my_list.sort(key=lambda element: element[1], reverse=True)

print(my_list)
