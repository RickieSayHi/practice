"""
对文件的写入
"""

# f = open("C:\CodeWorkingPlace\MyselfProjects\PycharmProjects\stest.txt", "w", encoding="UTF-8")
#
# f.write("这是一个测试，写入文件内容")
# f.flush()
# f.close()

h = open("C:\CodeWorkingPlace\MyselfProjects\PycharmProjects\stest.txt", "a", encoding="UTF-8")
h.write("新增一条内容")
h.close()


h = open("C:\CodeWorkingPlace\MyselfProjects\PycharmProjects\stest.txt", "a", encoding="UTF-8")
h.write("\n\n新增一条内容,2022年9月15日09:34:24")
h.close()
