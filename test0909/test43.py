"""
作业： 从MySQL数据库中读取数据，然后将数据以json数据的格式写入到文件中
将 test42 文件中写入数据库中的数据读取出来，再反向写出为如下的文件
"""
import datetime

from pymysql import Connection

# 1、从数据库中读取目标数据
conn = Connection(
    host="192.168.1.107",
    port=3306,
    user="root",
    password="qwer1234",
    autocommit=True,
    database="py_sql"
)
results = []
cursor = conn.cursor()
try:
    sql = "select * from orders"
    cursor.execute(sql)
    results = cursor.fetchall()
    # for record in results:
    #     print(record)
except Exception as e:
    print(f"程序异常，异常原因为： {e}")

conn.close()


# 2、将读取到的数据写入文本文件中
data_list = []
f = open("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/output_mysql_data.txt", "a", encoding="UTF-8")
for record in results:
    data_dict = {"date": record[0], "order_id": record[1], "money": record[2], "province": record[3]}

f.close()

# for record in results:
    # my_date: datetime = record[0]
    # my_date.isoformat()
    # print(my_date)
    # my_date.strftime("%Y-%m-%d %H:%M:%S")
    # print(my_date)

    # b = datetime.datetime.now()
    # print(b)
    # b.isoformat()
    # print(b)
    # b.strftime("%Y-%m-%d %H:%M:%S")
    # print(b)

    # print(record[0])
    # print(record[1])
    # print(record[2])
    # print(record[3])

