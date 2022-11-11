def str_reverse(s):
    """
    这是一个反转字符串内容的方法
    :param s: 传入的字符串参数
    :return:  返回反转后的字符串
    """
    print(f"传入的参数是： {s}")
    return s[::-1]

    # # 将字符串反转后返回
    # s_list = list(s)
    # s_list.reverse()
    # return str(s_list)


def substr(s, x, y):
    """
    功能：使用序列切片对字符串进行切割
    :param s:  传入的字符串
    :param x:  切片开始的下标 （包括开始下标）
    :param y:  切片结束的下标 （不包括结束下标）
    :return:   切片后的字符串
    """
    print(f"传入的参数是： {s, x, y}")
    return s[x: y]

    # # 按照下标 x , y, 对字符串 s 进行切片，将结果以 list 的形式返回
    # first = s[x]
    # second = s[y]
    # first_list = s.split(first)
    # second_list = first_list[1].split(second)
    # print(f"分割后的列表 first 为： {first_list}")
    # print(f"分割后的列表 second 为： {second_list}")
    # result = f"{first}{second_list[0]}{second}"
    # print(f"分割后的结果 为： {result}")
    # return result


# 加入判断当前文件执行是 导入还是自身执行
# 不进入if判断里，说明是作为导入文件执行的，if中的代码将不被执行
if __name__ == '__main__':
    # 表示当前文件是直接运行的
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员", 1, 3))
