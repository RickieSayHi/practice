"""
数据 字符串容器
"""


my_str = "  it's itheima and itcast suoyou de yiqi    "
print(f"原始字符串是： {my_str}")
my_str.strip()
print(f"去除前后空格后的是： {my_str}")
my_str = "12122323414  it's itheima and itcast suoyou de yiqi   32324412121 "
my_str.strip("12")
print(f"去除指定元素后的字符串为： {my_str}")


new_str = "itherma itcast boxuegu"
print(f"旧的字符串为： {new_str}")
count = new_str.count("it")
print(f"统计字符串中有 {count} 个 'it' 字符")
new_str = new_str.replace(" ", "|")
print(f"新的字符串为： {new_str}")
strArr = new_str.split("|")
print(f"得到的列表为： {strArr}")


str_test = "万过薪月，员序程马黑来，nohtyP学"
print(f"初始化字符串为： {str_test}")
# 请使用学过的任何方式，得到“黑马程序员”
new_str_test = str_test[::-1]
print(f"倒序字符串为： {new_str_test}")
arr_str = new_str_test.split('，')
target = arr_str[1]
print(f"目标字符串为： {target}")
target = "来黑马程序员来来"
target = target.strip("来")
print(f"目标字符串为： {target}")