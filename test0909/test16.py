"""
容器之间的区别
"""

my_list = [1, 2, 3, 4, 5, 6]
my_tuple = (1, 2, 3, 4, 5, 6)
my_string = "123456789"
my_set = {1, 2, 3, 4, 5, 6, 7}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5, "key6": 6}

# len元素的个数
print(f"列表    \t元素的个数为：  {len(my_list)}")
print(f"元组    \t元素的个数为：  {len(my_tuple)}")
print(f"字符串  \t元素的个数为：  {len(my_string)}")
print(f"集合    \t元素的个数为：  {len(my_set)}")
print(f"字典    \t元素的个数为：  {len(my_dict)}")

# max 最大元素是
print(f"列表    \t最大元素为：  {max(my_list)}")
print(f"元组    \t最大元素为：  {max(my_tuple)}")
print(f"字符串  \t最大元素为：  {max(my_string)}")
print(f"集合    \t最大元素为：  {max(my_set)}")
print(f"字典    \t最大元素为：  {max(my_dict)}")

# max 最小元素是
print(f"列表    \t最小元素为：  {min(my_list)}")
print(f"元组    \t最小元素为：  {min(my_tuple)}")
print(f"字符串  \t最小元素为：  {min(my_string)}")
print(f"集合    \t最小元素为：  {min(my_set)}")
print(f"字典    \t最小元素为：  {min(my_dict)}")