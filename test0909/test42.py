"""
MySQL 综合案例
"""

from pymysql import Connection
from test40_file_define import TextFileReader, JsonFileReader
from test40_data_define import Record

text_file_reader = TextFileReader("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年2月销售数据.txt")

text_data = text_file_reader.read_data()
json_data = json_file_reader.read_data()

all_data = text_data + json_data
# 打印拿到的数据
# for record in all_data:
#     print(record)

# 构建MySQL数据库链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="qwer1234",
    autocommit=True
)
# 获取游标对象
cursor = conn.cursor()

try:
    # 选择数据库
    conn.select_db("py_sql")
    # 创建表
    cursor.execute(
        "create table if not exists orders(order_date date, order_id varchar(255), money int, province varchar(10))")
    # 组织SQL语句
    for record in all_data:
        sql = f"insert into orders(order_date, order_id, money, province)" \
              f"values('{record.date}', '{record.order_id}', '{record.money}', '{record.province}') "
        # print(sql)
        # 执行SQL语句
        cursor.execute(sql)

except Exception as e:
    print(f"程序异常，异常原因是： {e}")

# 关闭MySQL数据库链接对象
conn.close()
