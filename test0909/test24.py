# 使用自定义的包
from my_utils import str_util
import my_utils.file_util

str_result = str_util.str_reverse("abcdefg")
print(f"倒序后的字符串内容为： {str_result}")
print("=========================")
s = str_util.substr("ius8jdeijddcx", 3, 7)
print(f"返回的结果是： {s}")

# 对文件进行操作
my_utils.file_util.print_file_info("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/1234.txt")
my_utils.file_util.append_to_file("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/12abc.txt", "这是追加的内容，2022年9月15日13:26:10")
