"""
字典的常用操作: 练习：升职加薪
"""

my_dict = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    }, "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    }, "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    }, "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    }, "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

print(f"员工信息如下： {my_dict}")

for key in my_dict:
    user = my_dict[key]
    level = int(user["级别"])
    if level == 1:
        user["级别"] = level + 1
        user["工资"] = int(user["工资"]) + 1000

print(f"加薪后信息为： {my_dict}")

for name in my_dict:
    if my_dict[name]["级别"] == 2:
        my_dict[name]["级别"] = 3
        my_dict[name]["工资"] += 1000

print(f"再次升职加薪： {my_dict}")
