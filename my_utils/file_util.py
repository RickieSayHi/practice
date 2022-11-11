def print_file_info(file_name):
    """
    功能是： 将给定路径的文件内容输出到控制台中
    :param file_name: 即将读取的文件路径
    :return: None
    """
    print(f"file_name = {file_name}")
    fr = None
    try:
        fr = open(file_name, "r", encoding="UTF-8")
        content = fr.read()
        print("文件的全部内容为：")
        print(content)
    except Exception as e:
        print(f"程序出现异常了，原因是： {e}")
    finally:
        if fr:  # 如果变量是None，表示False；如果有任何内容，就表示True
            fr.close()


def append_to_file(file_name, data):
    """
    功能是：将指定的数据追加到指定的文件中
    :param file_name: 指定的文件路径
    :param data:      指定的数据
    :return:          None
    """
    print(f"file_name = {file_name} , data = {data}")
    fw = open(file_name, "a", encoding="UTF-8")
    fw.write(data)
    fw.write("\n")
    fw.close()


if __name__ == '__main__':
    print_file_info("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/bill.txt")
    append_to_file("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/test_append.txt", "黑马程序员")
