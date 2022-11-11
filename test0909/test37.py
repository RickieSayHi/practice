"""
设计带有私有成员的手机
"""


class Phone:
    __is_5g_enable = True
    type = "SanXing"

    def funcCall(self):
        print("拨打电话")

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g未开启")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中。。。。")


phone = Phone()
phone.call_by_5g()

from my_util_package import my_util_string
from my_util_package import my_util_file


def func_string(s):
    print(f"反转前的字符串为： {s}")
    s = my_util_string.str_reverse(s)
    print(f"反转后的字符串为： {s}")


def func_substr(s, x, y):
    print(f"截取前的字符串： {s}")
    s = my_util_string.substr(s, x, y)
    print(f"截取后的字符串： {s}")


func_string("黑马程序员")

func_substr("这是一篇好文章", 2, 5)


my_util_file.print_file_info("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/my_test.txt")

my_util_file.append_to_file("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/my_test.txt", "5555")

my_util_file.print_file_info("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/my_test.txt")

my_util_file.append_to_file("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/my_test.txt", "6666")

my_util_file.print_file_info("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/my_test.txt")