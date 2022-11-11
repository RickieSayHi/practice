"""
数据库链接和操作
"""

from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="qwer1234"
)

# 打印数据库服务信息
# print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()

# 先选择数据库
conn.select_db("world")

# 使用游标对象，执行SQL语句
# cursor.execute(
#     "create table student(id int , name varchar(20), age int, tel varchar(20))")

cursor.execute(
    "insert into student values (3, 'cc', 18, '18700004444'), (4, 'dd', 19, '18800001234')")

# 执行SQL语句后，需要将事务进行提交确认
conn.commit()

# 使用数据库，记得要及时关闭数据库，防止占用数据库连接
conn.close()
