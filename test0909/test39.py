"""
数据分析案例
某公司，有2分数据文件，现需要对其进行分析处理，计算每日的销售额并以柱状图标的形式进行展示。
"""
import json
from pyecharts.charts import Bar


class Sales:
    def __init__(self, date, sale_id, sale, province):
        self.date = date
        self.sale_id = sale_id
        self.sale = sale
        self.province = province

    def __str__(self):
        return f"date: {self.date}, order_id: {self.sale_id}, sale: {self.sale}, province: {self.province}"


data_list = []

f1 = None
try:
    f1 = open("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年1月销售数据.txt", "r", encoding="UTF-8")
    for line in f1.readlines():
        line = line.strip()
        arr = line.split(",")
        data = Sales(arr[0], arr[1], arr[2], arr[3])
        data_list.append(data)
except Exception as e:
    print(f"程序出现异常，异常原因为：{e}")
finally:
    if f1:
        f1.close()

f2 = None
try:
    f2 = open("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年2月销售数据.txt", "r", encoding="UTF-8")
    for line in f2.readlines():
        print(f"line = {line}")
        # 将字符串转变为json字符串
        json_str = json.loads(line)
        # 将json字符串转成字典
        my_dict = dict(json_str)
        print(f"my_dict = {my_dict}")
        # 将数据填充到类对象中，并加入到数据列表中
        data = Sales(my_dict["date"], my_dict["order_id"], my_dict["money"], my_dict["province"])
        data_list.append(data)
except Exception as e:
    print(f"程序出现异常，异常原因为：{e}")
finally:
    if f2:
        f2.close()

for data in data_list:
    print(f"data = {data}")

# 分析数据，并生成数据图表
