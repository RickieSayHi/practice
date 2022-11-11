"""
操作数据库的练习
"""

from pymysql import Connection

# 构建到 MySQL 数据库的链接
conn = Connection(
    host="localhost",  # 主机名（IP）
    port=3306,  # 端口，默认3306
    user="root",  # 账户名
    password="qwer1234",  # 密码
    autocommit=True  # 自动提交（确认）
)
# 打印获取到数据库服务的信息
print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()  # 获取到游标对象

try:
    # 选择数据库
    conn.select_db("world")
    # 执行sql
    # cursor.execute("create table test_pymysql(id int)")

    # 执行查询性质SQL
    cursor.execute("select * from student")

    results = cursor.fetchall()
    for x in results:
        print(x)

    cursor.execute("insert into student values (5, '王大发', 33, '男')")
    # 手动 通过连接对象 确认，提交事务
    # conn.commit()
except Exception as e:
    print(f"程序异常，异常原因为： {e}")

# 关闭链接
conn.close()
