"""
练习对文件进行读取操作
"""

f = open('C:\CodeWorkingPlace\MyselfProjects\PycharmProjects\word.txt', 'r', encoding='UTF-8')

my_str = f.read()
print(f"读取返回的数据类型为： {type(my_str)}")
print(f"获取 读取的内容为： \n{my_str}")
# 字符串中统计子字符串出现的个数
count = my_str.count('itheima')
print(f"itheima 出现的次数为： {count}")

my_str = my_str.replace('\n', ' ')
my_list = my_str.split(' ')
print(f"获取到列表为： {my_list}")

count = 0
for word in my_list:
    if word == 'itheima':
        count += 1

print(f"该文件中 共有 出现'itheima' 单词 {count} 次")

f.close()