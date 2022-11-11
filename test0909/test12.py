"""
元祖的操作
"""


# 定义一个元祖
t1 = ("1", "2", 3, 4, ["hello", "world"])
print(f"修改前的元祖内容为： {t1}")
t1[4][0] = "Hi"
t1[4].append(["8", "9", "10"])
print(f"修改后的元祖内容为： {t1}")


t2 = ('周杰伦', 11, ['football', 'music'])
print(f"初始化元祖的内容为： {t2}")
# 1/查询年龄所在的下标位置
index = t2.index(11)
print(f"年龄所在的位置下标为： {index}")
# 2/查询学生的姓名
name = t2[0]
print(f"学生的姓名为： {name}")
# 3/删除学生爱好中的football
t2[2].remove("football")
print(f"删除 football 后的元祖内容为： {t2}")
# 4/增加爱好：coding到爱好list内
t2[2].append("coding")
print(f"添加爱好coding到爱好list中，元祖内容为： {t2}")