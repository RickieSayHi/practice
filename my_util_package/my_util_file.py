"""
创建一个自定义包，名称为： my_utils （我的工具包）
在包内提供2个模块
str_util.py  (字符串相关工具, 内含：)
1/函数: str_reverse(s), 接收传入字符串，将字符串反转返回
2/函数: substr(s,x,y),按照下标x和y，对字符串进行切片

file_util.py (文件处理相关工具，内含：）
1、函数： print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
2、函数： append_to_file(file_name, data)，接收文件路径以及传入数据，将数据追加写入文件中
"""


# 1、函数： print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(f"打印每一行的内容： {line}")
    except Exception as e:
        print(f"读取文件异常，异常内容为： {e}")
    finally:
        # 判断一下，如果文件不存在，就不需要关闭文件
        if f:
            f.close()


# 2、函数： append_to_file(file_name, data)，接收文件路径以及传入数据，将数据追加写入文件中
def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()
