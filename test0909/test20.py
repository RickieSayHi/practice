"""
文件操作综合案例
"""

"""
name, date, money, type, remarks
周杰轮,2022-01-01,100000,消费,正式
周杰轮,2022-01-02,300000,收入,正式
周东轮,2022-01-03,100000,消费,测试
林俊节,2022-01-01,300000,收入,正式
林俊节,2022-01-02,100000,消费,测试
林俊节,2022-01-03,100000,消费,正式
林俊节,2022-01-04,100000,消费,测试
林俊节,2022-01-05,500000,收入,正式
张学油,2022-01-01,100000,消费,正式
张学油,2022-01-02,500000,收入,正式
张学油,2022-01-03,900000,收入,测试
王力鸿,2022-01-01,500000,消费,正式
王力鸿,2022-01-02,300000,消费,测试
王力鸿,2022-01-03,950000,收入,正式
刘德滑,2022-01-01,300000,消费,测试
刘德滑,2022-01-02,100000,消费,正式
刘德滑,2022-01-03,300000,消费,正式
"""

# 需要做的是： 1、读取文件； 2、将文件写出到bill.txt.bak文件作为备份； 3、同时，将文件内标记为测试的数据行丢弃

fr = open("C:\CodeWorkingPlace\MyselfProjects\PycharmProjects\\bill.txt", "r", encoding="UTF-8")
fw = open("C:\CodeWorkingPlace\MyselfProjects\PycharmProjects\\bill.txt.bak", "w", encoding="UTF-8")

for line in fr:
    line = line.strip()
    print(f"读取每一行的内容为： {line}")
    line_list = line.split(",")
    if line_list[-1] == "测试":
        continue
    fw.write(line)
    fw.write("\n")

fr.close()
fw.close()
