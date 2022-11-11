"""
集合的操作
"""

set1 = {1, 2, 3, 4, 5, 6, 7}
num1 = len(set1)
print(f"集合的长度为： {num1} 个")

# 信息去重
# 有如下列表对象：
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
print(f"去重前的 列表是： {my_list}")
my_set = set()

for element in my_list:
    my_set.add(element)
print(f"去重后的 集合是： {my_set}")
